from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loggin', views.loggin, name='loggin'),
    path('signup', views.signup, name='signup'),
    path('student', views.student, name='student'),
]
