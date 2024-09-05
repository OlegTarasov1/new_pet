from rest_framework import permissions
from .models import Notes

class UuidPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in ['POST', 'PUT', 'PATCH']:
                if request.user.id == Notes.objects.get(id = request.data['id']).creator:
                    return True
                else:
                    return False
            elif request.method in ['GET', 'HEAD', 'OPTIONS']:
                return True
            else:
                return False
        else:
            return False