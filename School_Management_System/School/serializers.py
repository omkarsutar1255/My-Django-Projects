from django.db import models
from rest_framework import serializers
from .models import Student, School


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'username', 'school']


class SchoolSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = ['id', 'name', 'email', 'city', 'pincode', 'student']

