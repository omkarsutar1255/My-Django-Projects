from django.db import models


# Create your models here.
class employee(models.Model):
    Email = models.EmailField()
    Text = models.CharField(max_length=300)
