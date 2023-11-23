from django.urls import path
from . import views

urlpatterns = [
    path('user/signup', views.Signup.as_view(), name='signup'),
    path('user/login', views.Login.as_view(), name='login'),
    path('user/update/profile', views.Update.as_view(), name='update'),
    path('user/delete/account', views.Delete.as_view(), name='delete'),
    path('user/personal/accountsinfo', views.Accountsinfo.as_view(), name='accountsinfo'),
]