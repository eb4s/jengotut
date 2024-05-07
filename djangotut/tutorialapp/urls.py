from os import urandom
from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('studentform/', views.studentform, name='studentform'),
    path('teacherform/', views.teacherform, name='teacherform'),
    path('register/', views.register, name="register" ),
    path('profile/', views.profile, name="profile" ),

]