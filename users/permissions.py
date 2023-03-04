from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User
import ipdb


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # if request.user.is_authenticated and request.user.is_superuser:
        #     return True

        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class IsAuthenticatedOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        
        if request.user.id == obj.id:
            return True
        
        return False
