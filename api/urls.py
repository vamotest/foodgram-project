from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (FavoriteViewSet, IngredientViewSet, PurchaseViewSet,
                    SubscriptionViewSet)

router_v1 = DefaultRouter()
router_v1.register(r'ingredients', IngredientViewSet, basename='ingredients')
router_v1.register(
    r'subscriptions',
    SubscriptionViewSet,
    basename='subscriptions',
)
router_v1.register(r'favorites', FavoriteViewSet, basename='favorites')
router_v1.register(r'purchases', PurchaseViewSet, basename='purchases')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
