from rest_framework import serializers
from .models import MoviesData


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesData
        fields = ['Name', 'Budget', 'Description', 'Genres', 'Popularity',
                  'Revenue', 'Duration', 'Language', 'Status', 'Release_Date']
