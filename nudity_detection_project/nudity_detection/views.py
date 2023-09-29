# nudity_detection/views.py

from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage
import tensorflow as tf
import numpy as np
from nudenet import NudeClassifier
classifier = NudeClassifier()

def predict_nudity(image_path):
    # Load your nudity detection model
    result = classifier.classify(image_path)
    for i in result:
        print(result[i])
        print("safe percentage = ", result[i]['safe'])
        if result[i]['safe'] > result[i]['unsafe']:
            print("Safe Image = ", i)

    
    # You can use the prediction result to determine nudity or not
    # In this example, we assume a threshold value of 0.5
    if result[i]['unsafe'] >= 0.5:
        return "Nudity Detected"
    else:
        return "No Nudity Detected"

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()

            # Get the uploaded image's path and make a prediction
            image_path = image.image.path
            prediction_result = predict_nudity(image_path)

            # Save the prediction result
            image.prediction_result = prediction_result
            image.save()

            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = UploadedImage.objects.all()
    return render(request, 'image_list.html', {'images': images})
