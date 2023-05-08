from django.urls import path
from app import views

urlpatterns = [
    path('api/', views.StudentAPI.as_view()),
    path('api/<int:pk>/', views.StudentAPI.as_view()),
]
