from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'password', 'full_name', 'phone_number', 'gender', 'age', 'profile_pic', 'state', 'status']
    list_display = ('email', 'full_name', 'phone_number', 'gender', 'age', 'state')
