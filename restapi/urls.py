"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from . import views
from rest_framework import urls
# from .views import redirect_homepage

from cars import urls, views
from cars.views import cars_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/base-auth', include('rest_framework.urls')),
    path("api/v1/cars/", include('cars.urls')),

    path('api/v1/', views.cars_index, name='cars_url'),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),

    path('api/v1/base-auth/', include('rest_framework.urls')),
    path("api/v1/cars/", include('cars.urls')),
    path('api/v1/cars/usercars/', views.UserListView, name = 'user_cars'),
]

urlpatterns += [
    path('api/v1/accounts/', include('django.contrib.auth.urls'), name = 'login_url'),
    # path('api/v1/auth/users/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UserActivationView),
    
]
