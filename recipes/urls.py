from django.urls import include, path

from recipes.views import recipe_new
from recipes.views import recipe_edit
from recipes.views import recipe_delete
from recipes.views import recipe_view_slug
from recipes.views import recipe_view_redirect
from recipes.views import purchases
from recipes.views import purchases_download
from recipes.views import index
from recipes.views import subscriptions
from recipes.views import favorites
from recipes.views import profile_view

recipes_urls = [
    path('new/', recipe_new, name='recipe_new'),
    path('<int:recipe_id>/<slug:slug>/edit/', recipe_edit, name='recipe_edit'),
    path(
        '<int:recipe_id>/<slug:slug>/delete/',
        recipe_delete, name='recipe_delete'
    ),
    path(
        '<int:recipe_id>/<slug:slug>/',
        recipe_view_slug, name='recipe_view_slug'
    ),
    path(
        '<int:recipe_id>/', recipe_view_redirect,
        name='recipe_view_redirect'
    ),
]

purchases_urls = [
    path('', purchases, name='purchases'),
    path('download/', purchases_download, name='purchases_download'),
]


urlpatterns = [
    path('', index, name='index'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('favorites/', favorites, name='favorites'),
    path('purchases/', include(purchases_urls)),
    path('recipe/', include(recipes_urls)),
    path('<str:username>/', profile_view, name='profile_view'),
]
