from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, SubscriptionViewSet

router_v1 = DefaultRouter()
router_v1.register(r'ingredients', IngredientViewSet, basename='ingredients')
router_v1.register(
    r'subscriptions',
    SubscriptionViewSet,
    basename='subscriptions',
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
