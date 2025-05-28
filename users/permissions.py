from rest_framework import permissions


class IsStaffUser(permissions.BasePermission):
    """
    Checks if the user is is_staff.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
