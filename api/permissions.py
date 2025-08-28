from rest_framework import permissions

<<<<<<< HEAD
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return getattr(obj, "owner", None) == request.user
=======

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Superuser has full access
        if request.user and request.user.is_superuser:
            return True
        # Otherwise, must be the owner
        return getattr(obj, "owner", None) == request.user
>>>>>>> feature/reports-api
