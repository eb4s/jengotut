from os import urandom
from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
]