from decimal import Decimal

from django.conf import settings
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404

from .models import Ingredient, RecipeIngredient


def get_paginated_view(request, some_list):
    paginator = Paginator(some_list, settings.PAGINATION_PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page, paginator


def get_request_tags(request):
    return request.GET.getlist('tag', ('breakfast', 'lunch', 'dinner'))


def get_ingredients(request):
    ingredients = {}
    post = request.POST
    for key, name in post.items():
        if key.startswith('nameIngredient'):
            num = key.partition('_')[-1]
            ingredients[name] = post[f'valueIngredient_{num}']
    return ingredients


def save_recipe(request, form):
    with transaction.atomic():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()

        objs = []
        ingredients = get_ingredients(request)

        for name, quantity in ingredients.items():
            ingredient = get_object_or_404(Ingredient, title=name)
            objs.append(
                RecipeIngredient(
                    recipe=recipe,
                    ingredient=ingredient,
                    quantity=Decimal(quantity.replace(',', '.'))
                )
            )

        RecipeIngredient.objects.bulk_create(objs)
        form.save_m2m()
        return recipe


def edit_recipe(request, form, instance):
    with transaction.atomic():
        RecipeIngredient.objects.filter(recipe=instance).delete()
        return save_recipe(request, form)
