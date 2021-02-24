from rest_framework.permissions import SAFE_METHODS, BasePermission

from api.models.user import User


class IsUser(BasePermission):
    allowed_user_roles = User.USER

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False


class IsModerator(BasePermission):
    allowed_user_roles = User.MODERATOR

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.author == request.user
        else:
            return False


class IsAdmin(BasePermission):
    allowed_user_roles = User.ADMIN

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False


class IsGetOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff
