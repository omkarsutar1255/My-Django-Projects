from django.urls import path
from Main_Interface import views


urlpatterns = [
    path("", views.Flipkart, name="Flipkart"),
    # path("details", views.SaveDetails, name="Details"),
    path("fetchdetails", views.fetchdetails, name="fetchdetails"),
]