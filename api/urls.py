from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import FavoriteViewSet
from api.views import IngredientViewSet
from api.views import PurchaseViewSet
from api.views import SubscriptionViewSet

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
