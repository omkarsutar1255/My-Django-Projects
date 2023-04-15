from django.contrib import admin
from .models import School, Student


# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'city', 'pincode']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'school']
