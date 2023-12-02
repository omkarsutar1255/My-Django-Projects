from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime, timezone
from .permissions import IsOwnerOrReadOnly

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
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(responsedata(True, "User Created Successfullly",serializer.data),
                                status=status.HTTP_200_OK)
            else:
                return Response(responsedata(False, "Something went wrong",serializer.errors),
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data.get('username')
                password = serializer.data.get('password')
                user = authenticate(username=username, password=password)
                if user is None:
                    return Response(responsedata(False, "Invalid password"), status=status.HTTP_400_BAD_REQUEST)
                token_data = get_tokens_for_user(user)
                return Response(responsedata(True, "User Successfully Logged", token_data), status=status.HTTP_200_OK)
            return Response(responsedata(False, "Invalid Login Credential", serializer.errors),
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

class VendorAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            print("1 = ", data, request.user)
            data['user'] = request.user.id
            print("2 = ", data)
            serializer = VendorSerializer(data=data)
            print("3 = ", serializer)
            if serializer.is_valid():
                print("4")
                serializer.save()
                return Response(responsedata(True, "Vendor Created Successfullly",serializer.data),
                                status=status.HTTP_200_OK)
            else:
                return Response(responsedata(False, "Something went wrong",serializer.errors),
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            vendors = Vendor.objects.all()
            serializer = VendorSerializer(vendors, many=True)
            return Response(responsedata(True, "Data", serializer.data), status=status.HTTP_200_OK)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

class VendorDataAPI(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, id=None):
        try:
            vendor = Vendor.objects.get(vendor_code=id)
            serializer = VendorSerializer(vendor)
            return Response(responsedata(True, "Data", serializer.data), status=status.HTTP_200_OK)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            vendor = Vendor.objects.get(vendor_code=id)
            self.check_object_permissions(request, vendor)
            serializer = VendorSerializer(vendor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(responsedata(True, "Data updated", serializer.data), status=status.HTTP_200_OK)
            else:
                return Response(responsedata(False, "Something went wrong", serializer.errors),
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            vendor = Vendor.objects.get(vendor_code=id)
            self.check_object_permissions(request, vendor)
            vendor.delete()
            return Response(responsedata(True, "Deleted"), status=status.HTTP_200_OK)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)), status=status.HTTP_400_BAD_REQUEST)

######################################################################################################################

class PurchaseOrderAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            data = request.data
            vendor_name = data.get('vendor_name')
            if not vendor_name:
                return Response(responsedata(False, "Vendor name is required"),
                                status=status.HTTP_400_BAD_REQUEST)

            vendor = Vendor.objects.get(name=vendor_name)
            data['vendor'] = vendor.id
            data['user'] = request.user.id

            serializer = PurchaseOrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(responsedata(True, "Purchase Order Created Successfullly",serializer.data),
                                status=status.HTTP_200_OK)
            else:
                return Response(responsedata(False, "Something went wrong",serializer.errors),
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            purchaseorder = PurchaseOrder.objects.all()
            serializer = PurchaseOrderSerializer(purchaseorder, many=True)
            return Response(responsedata(True, "Data", serializer.data), status=status.HTTP_200_OK)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderDataAPI(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, id=None):
        try:
            purchaseorder = PurchaseOrder.objects.get(po_number=id)
            serializer = PurchaseOrderSerializer(purchaseorder)
            return Response(responsedata(True, "Data", serializer.data), status=status.HTTP_200_OK)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        
        try:
            print("Inside Put")
            purchaseorder = PurchaseOrder.objects.get(po_number=id)
            self.check_object_permissions(request, purchaseorder)
            serializer = PurchaseOrderSerializer(purchaseorder, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(responsedata(True, "Data updated", serializer.data), status=status.HTTP_200_OK)
            else:
                return Response(responsedata(False, "Something went wrong", serializer.errors),
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            purchaseorder = PurchaseOrder.objects.get(po_number=id)
            self.check_object_permissions(request, purchaseorder)
            purchaseorder.delete()
            return Response(responsedata(True, "Deleted"), status=status.HTTP_200_OK)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)), status=status.HTTP_400_BAD_REQUEST)

#######################################################################################################################
class PerformanceAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        try:
            vendor = Vendor.objects.get(vendor_code=id)
            serializer = PerformanceSerializer(vendor)
            return Response(responsedata(True, "Data", serializer.data), status=status.HTTP_200_OK)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)), status=status.HTTP_400_BAD_REQUEST)

class OrderAcknowledge(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id=None):
        try:
            purchaseorder = PurchaseOrder.objects.get(po_number=id)
            purchaseorder.acknowledgment_date = datetime.now()
            purchaseorder.save()
            return Response(responsedata(True, "Purchase order acknowledged"),
                            status=status.HTTP_200_OK)
        except Exception as err:
            return Response(responsedata(False, "Something went wrong", str(err)),
                                status=status.HTTP_400_BAD_REQUEST)
