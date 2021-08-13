from django.contrib.auth import login
from django.urls import path
from .views import main_page, create_ad, all_cars


urlpatterns = [
    path('cars', all_cars, name='cars'),
    path('create', create_ad, name='create_ad'),
    path('', main_page, name='main_page'),
]
