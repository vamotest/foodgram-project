from django.contrib.auth import get_user_model
from django.shortcuts import render

from .models import Recipe, Tag
from .utils import get_paginated_view, request_tags

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
