from django.contrib.flatpages import views
from django.urls import include, path

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('users.urls')),
]

urlpatterns += [
    path('about/', include('django.contrib.flatpages.urls')),
    path('author/', views.flatpage, {'url': '/author/'}, name='author'),
    path('tech/', views.flatpage, {'url': '/tech/'}, name='tech'),
]