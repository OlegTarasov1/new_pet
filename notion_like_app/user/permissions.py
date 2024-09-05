from rest_framework import permissions

class UserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return True
        else:
            if request.user == obj or request.user.is_staff:
                return True
            else:
                return False