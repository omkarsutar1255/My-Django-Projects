from django.contrib import admin
from .models import employee


# Register your models here.
@admin.register(employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'Email', 'Text']
