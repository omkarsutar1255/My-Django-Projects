from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('movieapi', views.MovieModelViewSet, basename='student')


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
]


