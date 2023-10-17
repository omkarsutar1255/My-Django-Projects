from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("add", views.add, name='add'),
    path("edit", views.edit, name='edit'),
    path("update/<str:id>", views.update, name='update'),
    path("delete/<str:id>", views.delete, name='delete'),
    path("pic", views.pic, name='pic'),
]
