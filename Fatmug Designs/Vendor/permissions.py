# permissions.py
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        print("inside object has permission")
        if request.method == 'GET':
            return True
        if request.method in ['PUT', 'DELETE']:
            print("User permission = ", obj.user, request.user)
            return obj.user  == request.user
        return False
