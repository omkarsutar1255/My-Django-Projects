from django.contrib import admin
from .models import MoviesData


# Register your models here.
@admin.register(MoviesData)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Budget', 'Description', 'Genres', 'Popularity',
                    'Revenue', 'Duration', 'Language', 'Status', 'Release_Date']
