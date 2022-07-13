from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            # If method is get, API will be accessible
            return True
        return False
