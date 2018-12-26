from rest_framework import permissions


class IsDirectorOrAdmin(permissions.BasePermission):
    """
    only directors and admin
    """

    def has_permission(self, request, view):
        return request.user.user_type == 4 or request.user.is_staff


class IsCoachDirectorOrReadOnly(permissions.BasePermission):
    """
    Permission to only allow coaches, directors, or admin to view and edit
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_type in (3, 4) or request.user.is_staff


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Only allows users admin users edit rights. All others view only
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_staff

class IsAppropriateUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.id:
            return True
        elif request.user.id == obj.team.coach.id:
            return True
        elif request.user.id == obj.team.club.director.id:
            return True
        elif request.user.is_staff:
            return True

        return False


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.id:
            return True

        return False