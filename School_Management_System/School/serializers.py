from django.db import models
from rest_framework import serializers


class SchoolSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    city = serializers.CharField(max_length=100)
    pincode = serializers.IntegerField()
    password = serializers.CharField(max_length=32)
