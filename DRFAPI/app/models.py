from django.db import models


# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=20, null=False)
    Email = models.EmailField(max_length=50, unique=True)
    Phone_no = models.IntegerField()
    Address = models.CharField(max_length=40)


