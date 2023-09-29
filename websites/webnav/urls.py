from django.contrib import admin
from django.urls import path, include
from webnav import views

urlpatterns = [
    path('', views.index, name='index')
]
