from rest_framework.permissions import (
    AllowAny,
    SAFE_METHODS,
    BasePermission
)


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user and request.user.is_staff:
            return True

        return False


class CreateUserPermission(AllowAny):
    pass
