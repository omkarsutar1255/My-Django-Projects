from django.db import models
from django import forms

# Create your models here.
# class LoginForm(forms.Form):
#     user = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    address = models.TextField(null=True)
    phone_no = models.IntegerField(null=True)
    
    def __str__(self):
        print("self.name = ", self.name)
        return self.name