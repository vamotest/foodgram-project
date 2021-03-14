from rest_framework import filters, mixins, viewsets

from recipes.models import Ingredient

from .serializers import IngredientSerializer


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('^title',)
