from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('loggin', views.loggin, name='loggin'),
    path('signup', views.signup, name='signup'),
    path('signuppage', views.signuppage, name='signuppage'),
    path('student', views.student, name='student'),
]
