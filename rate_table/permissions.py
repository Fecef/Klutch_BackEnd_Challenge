from rest_framework import permissions
from rest_framework.views import View
from .models import RateTable


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: RateTable) -> bool:
        if request.method == "GET":
            return request.user.is_superuser

        return True
