from django.contrib import admin 
from django.urls import path, include
from . import views
from .views import (CarCreateView, CarsListView, CarDetailView, UserListView, CarDetail, CarCreate)
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'cars'
urlpatterns = [
    path('', views.cars_index, name='cars_url'),

    # path('registration/', RegisterUser.as_view(), name = 'reg_user'),

    path('car/create/', CarCreateView.as_view()),
    path('all/', CarsListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view(), name = 'car_detail'),  #/api/v1/cars/car/detail/8/
    # path('mylist/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    
    path('usercars/', UserListView.as_view(), name = 'all_cars'),
    path('usercars/<int:pk>/', CarDetail.as_view(), name = 'car_change'),

    # car_create
    # path('usercars/create/', views.car_create, name = 'create_page'),
    path('usercars/create/', views.CarCreate.as_view(), name = 'car_create')
    # path('usercars/<int:pk>/update/', CarUpdate.as_view(), name = 'car_change'),
    # path('usercars/<int:pk>/delete/', CarDelete.as_view(), name = 'car_change'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
 