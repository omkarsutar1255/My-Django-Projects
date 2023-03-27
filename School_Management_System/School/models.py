from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    name = models.TextField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    city = models.TextField(max_length=100)
    pincode = models.IntegerField()
    password = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    name = models.TextField(max_length=100, null=True)
    username = models.TextField(max_length=100)
    password = models.CharField(max_length=32)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
