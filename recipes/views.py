from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Recipe, Tag
from .utils import edit_recipe, get_paginated_view, request_tags, save_recipe

User = get_user_model()


def index(request):
    tags = request_tags(request)
    recipes = Recipe.objects.filter(tags__title__in=tags).select_related(
        'author').prefetch_related('tags').distinct()

    page, paginator = get_paginated_view(request, recipes)
    context = {
        'page': page,
        'paginator': paginator,
        'tags': tags,
        'all_tags': Tag.objects.all(),
    }
    return render(request, 'recipes/index.html', context)


@login_required
def recipe_new(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        recipe = save_recipe(request, form)

        return redirect(
            'recipe_view_slug', recipe_id=recipe.id, slug=recipe.slug
        )

    context = {'form': form}
    return render(request, 'recipes/form_recipe.html', context)


@login_required
def recipe_edit(request, recipe_id, slug):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if not request.user.is_superuser:
        if request.user != recipe.author:
            return redirect(
                'recipe_view_slug', recipe_id=recipe.id, slug=recipe.slug
            )

    form = RecipeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=recipe
    )

    if form.is_valid():
        edit_recipe(request, form, instance=recipe)
        return redirect(
            'recipe_view_slug', recipe_id=recipe.id, slug=recipe.slug
        )

    context = {'form': form, 'recipe': recipe}
    return render(request, 'recipes/form_recipe.html', context)


@login_required
def recipe_delete(request, recipe_id, slug):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user.is_superuser or request.user == recipe.author:
        recipe.delete()
    return redirect('index')


def recipe_view_slug(request, recipe_id, slug):
    recipe = get_object_or_404(
        Recipe.objects.select_related('author'),
        id=recipe_id,
        slug=slug
    )
    context = {'recipe': recipe}
    return render(request, 'recipes/single_page.html', context)


def profile_view(request, username):
    tags = request_tags(request)
    author = get_object_or_404(User, username=username)
    author_recipes = author.recipes.filter(
        tags__title__in=tags).prefetch_related('tags').distinct()

    page, paginator = get_paginated_view(request, author_recipes)
    context = {
        'author': author,
        'page': page,
        'paginator': paginator,
        'tags': tags,
        'all_tags': Tag.objects.all(),
    }
    return render(request, 'recipes/author_recipe.html', context)


def recipe_view_redirect(request, recipe_id):
    recipe = get_object_or_404(Recipe.objects.all(), id=recipe_id)
    return redirect('recipe_view_slug', recipe_id=recipe.id, slug=recipe.slug)


@login_required
def subscriptions(request):
    authors = User.objects.filter(
        following__user=request.user).prefetch_related('recipes').annotate(
        recipe_count=Count('recipes')).order_by('username')

    page, paginator = get_paginated_view(request, authors)
    context = {'page': page, 'paginator': paginator}
    return render(request, 'recipes/user_subscriptions.html', context)


@login_required
def favorites(request):
    tags = request_tags(request)
    recipes = Recipe.objects.filter(
        favored_by__user=request.user, tags__title__in=tags
    ).select_related('author').prefetch_related('tags').distinct()

    page, paginator = get_paginated_view(request, recipes)
    context = {
        'page': page,
        'paginator': paginator,
        'tags': tags,
        'all_tags': Tag.objects.all(),
    }
    return render(request, 'recipes/favorite.html', context)


@login_required
def purchases(request):
    recipes = request.user.purchases.all()
    return render(request, 'recipes/shop_list.html', {'recipes': recipes})


@login_required
def purchases_download(request):
    title = 'recipe__ingredients__title'
    dimension = 'recipe__ingredients__dimension'
    quantity = 'recipe__ingredients_amounts__quantity'

    ingredients = request.user.purchases.select_related('recipe').order_by(
        title).values(title, dimension).annotate(amount=Sum(quantity)).all()

    if not ingredients:
        return render(request, 'misc/400.html', status=400)

    text = 'Список покупок:\n\n'
    for number, ingredient in enumerate(ingredients, start=1):
        text += (
            f'{number}) '
            f'{ingredient[title]} - '
            f'{ingredient["amount"]} '
            f'{ingredient[dimension]}\n'
        )

    response = HttpResponse(text, content_type="text/plain")
    filename = 'shopping_list.txt'
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response
