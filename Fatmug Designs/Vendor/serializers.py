from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    def validate_password(self, str) -> str:
        """ A function to save the password for storing the values """
        return make_password(str)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username', 'password']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"

class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField(write_only=True)
    order_date = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(read_only=True)
    quality_rating = serializers.FloatField(read_only=True)
    issue_date = serializers.DateTimeField(read_only=True)
    acknowledgment_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
