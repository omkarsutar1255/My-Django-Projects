from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

def responsedata(status, message, data=None):
    if status:
        return {"status":status,"message":message,"data":data}
    else:
        return {"status":status,"message":message,"data":data}

# Create your views here.
from nudenet import NudeClassifier
classifier = NudeClassifier()

class index(APIView):
    def post(self, request):
        print("inside seller")
        print(request)
        if 'testimage' not in request.data:
            return Response({'error': 'Image not provided in the request'}, status=status.HTTP_400_BAD_REQUEST)
        image = request.data['testimage']
        print(image, type(image))
        result = classifier.classify(image)
        for i in result:
            print(result[i])
            print("safe percentage = ", result[i]['safe'])
            if result[i]['safe'] > result[i]['unsafe']:
                print("Safe Image = ", i)
        return Response(responsedata(True, "Product Images verified"), status=status.HTTP_200_OK)
