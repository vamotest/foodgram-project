from django.contrib import admin
from django.db.models import Count

from .models import Ingredient, Recipe, RecipeIngredient, Tag


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, )
    list_display = (
        'id', 'title', 'author', 'slug', 'cooking_time',
        'get_favorite_count', 'pub_date'
    )
    list_filter = ('author', 'tags__title')
    search_fields = ('title', 'author__username')
    autocomplete_fields = ('author', )
    ordering = ('-pub_date', )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(favorite_count=Count('favored_by'))
    
    @staticmethod
    def get_favorite_count(obj):
        return obj.favorite_count


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'dimension')
    search_fields = ('^title', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'color', 'display_name')
    list_filter = ('title', )
