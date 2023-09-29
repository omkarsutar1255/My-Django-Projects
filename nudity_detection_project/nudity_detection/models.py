# nudity_detection/models.py

from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    prediction_result = models.CharField(max_length=255, null=True, blank=True)
