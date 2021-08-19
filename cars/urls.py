from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login
from django.urls import path
from .views import main_page, create_ad, all_cars, car_detail, user_cars, car_update, car_delete, search

urlpatterns = [
    path('search/', search, name='search'),
    path('car-delete/<int:pk>/', car_delete, name='car_delete'),
    path('car-update/<int:pk>/', car_update, name='car_update'),
    path('my-cars/', user_cars, name='user_cars'),
    path('car/<int:pk>/', car_detail, name='car_detail'),
    path('cars', all_cars, name='cars'),
    path('create', create_ad, name='create_ad'),
    path('', main_page, name='main_page'),
]
