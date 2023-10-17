from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Harry Ice Cream Admin"
admin.site.site_title = "Harry Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Harry Ice Creams"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls'))
]