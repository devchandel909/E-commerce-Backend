from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):

    

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:

            return True

    
        return request.user.is_staff
    
    
    
    
    
    
    
    
    
    """
    GET requests:
        Everyone can access

    POST/PUT/DELETE:
        Only admin can access
    """
    
    
    
    
    
    
    
    
    
    '''
    
    class IsAdminOrReadOnly(BasePermission):

    

    def has_permission(self, request, view):

        # SAFE_METHODS means:
        # GET
        # HEAD
        # OPTIONS
        if request.method in SAFE_METHODS:

            return True

        # Write operations only for admin
        return request.user.is_staff '''