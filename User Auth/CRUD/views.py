from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import logging

logger = logging.getLogger('main')

def responsedata(status, message, data=None):
    if status:
        return {"status":status,"message":message,"data":data}
    else:
        return {"status":status,"message":message,"data":data}

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class Signup(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = CustomUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                # email = request.user.email
                # logger.info(f"{email} user data has Updated")
                return Response(responsedata(True, "User Created Successfullly",serializer.data), status=status.HTTP_200_OK)
            else:
                logger.error(serializer.errors)
                return Response(responsedata(False, "Something went wrong",serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            logger.error(err)
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data.get('email')
                password = serializer.data.get('password')
                user = authenticate(email=email, password=password)
                if user is None:
                    logger.warning("User is not Valid")
                    return Response(responsedata(False, "Invalid password"), status=status.HTTP_400_BAD_REQUEST)
                token_data = get_tokens_for_user(user)
                return Response(responsedata(True, "User Successfully Logged", token_data), status=status.HTTP_200_OK)
            logger.error(serializer.errors)
            return Response(responsedata(False, "Invalid Login Credential", serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            logger.error(err)
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

class Update(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = UpdateSerializer(request.user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                email = request.user.email
                logger.info(f"{email} user data has Updated")
                return Response(responsedata(True, "Updated", serializer.data), status=status.HTTP_200_OK)
            logger.error(serializer.errors)
            return Response(responsedata(False, "Invalid", serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            logger.error(err)
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

class Delete(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = DeleteSerializer(request.user, data=request.data)
            if serializer.is_valid():
                name = request.user.email
                request.user.delete()
                logger.info(f"{name} user has been deleted")
                return Response(responsedata(True, "Deleted", serializer.data), status=status.HTTP_200_OK)
            logger.error(serializer.errors)
            return Response(responsedata(False, "Invalid", serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            logger.error(err)
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

class Accountsinfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            serializer = GetSerializer(request.user)
            return Response(responsedata(True, "Data", serializer.data), status=status.HTTP_200_OK)
        except Exception as err:
            logger.error(err)
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)