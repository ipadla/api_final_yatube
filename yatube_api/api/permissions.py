from rest_framework import permissions


class IsObjectAuthor(permissions.BasePermission):
    """SAFE_METHODS allowed for all, PATCH, PUT, DELETE for object author."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
