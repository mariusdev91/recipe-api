from rest_framework import permissions
from rest_framework.exceptions import NotFound


class IsAuthenticatedOrNotFound(permissions.BasePermission):
    """
    Grants access if the user is authenticated, otherwise returns a 404.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        raise NotFound(detail="No such resource found.", code=404)
