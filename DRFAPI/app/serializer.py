from rest_framework import serializers
from .models import Student


# search for other serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'Name', 'Email', 'Phone_no', 'Address']
