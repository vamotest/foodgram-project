from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
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


def recipe_view_redirect(request, recipe_id):
    recipe = get_object_or_404(Recipe.objects.all(), id=recipe_id)
    return redirect('recipe_view_slug', recipe_id=recipe.id, slug=recipe.slug)
