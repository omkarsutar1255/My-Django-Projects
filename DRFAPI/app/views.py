from django.core.checks import messages
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import xlrd
from tablib import Dataset
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.
class StudentAPI(APIView):
    # separate get data
    def get(self, request, pk=None, format=None):
        id = pk
        print('id = ', id)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except:
                return Response({'msg': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # import pdb
        # pdb.set_trace()
        # learn signal - Done
        # sending the emails (otp sign in, etc.)
        # notifications and alert in django
        # Google Authentication and fb auth
        dataset = Dataset()
        print("request.FILES= ", request.FILES, len(request.FILES))
        excel_file = request.FILES
        try:
            new_persons = excel_file['files']
        except Exception as e:
            return Response({'msg': f'File not Found, details: {e}'})
        if not new_persons.name.endswith('xlsx'):
            return Response({'msg': 'only xlsx file allowed'})
        imported_data = dataset.load(new_persons.read(), format='xlsx')
        all_fields = Student._meta.fields
        if not len(all_fields) == len(imported_data.headers) + 1:
            return Response({'msg': 'Columns count mismatched'}, status=status.HTTP_400_BAD_REQUEST)
        for data in imported_data:
            if not data[0].replace(' ', '').isalpha():
                return Response({'msg': 'Only characters allowed'})
            # if type(data[2]) is not int:
            #     return Response({'msg': 'Only Numbers allowed'})
            serializerdata = {'Name': data[0], 'Email': data[1], 'Phone_no': data[2], 'Address': data[3]}
            serializer = StudentSerializer(data=serializerdata)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)

    def delete(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                stu.delete()
                return Response({'msg': 'Data Deleted'}, status=status.HTTP_200_OK)
            except:
                return Response({'msg': 'Data not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'msg': 'Id not provided'}, status=status.HTTP_400_BAD_REQUEST)
