from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
import uuid

class BaseModel(models.Model):
    """Base ORM model"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True

login_status = (('user', 'User'),
        ('admin', 'Admin'),)

def validate_status(value):
        valid_choices_1 = [choice[0] for choice in login_status]
        print(valid_choices_1, value)
        if value not in valid_choices_1:
            return False
        else:
            return True

class User(BaseModel, AbstractUser):
    username = None
    
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(unique=True, max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='images/')
    state = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=login_status, null=True, blank=True, validators=[validate_status])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
