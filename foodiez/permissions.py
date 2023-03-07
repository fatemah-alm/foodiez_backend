from rest_framework import permissions
from rest_framework.exceptions import APIException
from rest_framework import status

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'you are not authorized to create a recipe'

    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
    


class IsLogin(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if request.user:
            return True
        raise NeedLogin()


class NeedLogin(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'error': True, 'message': 'need login'}
    default_code = 'not_authenticated'