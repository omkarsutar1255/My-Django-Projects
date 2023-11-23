from .models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email', 'password', 'full_name', 'age', 'gender', 'state', 'phone_number', 'profile_pic', 'status']
    def validate_password(self, str) -> str:
        """ A function to save the password for storing the values """
        return make_password(str)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'age', 'gender', 'state', 'phone_number', 'profile_pic']

class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'age', 'gender', 'state', 'phone_number', 'profile_pic', 'status']