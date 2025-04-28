from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role=='admin'
# class IsHotelOwner(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role=='hotel_owner'
# class IsCustomer(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role=='customer'
# class IsDeliveryBoy(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role=='delivery_boy'
class IsAdminOrHotelOwner(BasePermission):
    """
    Custom permission to allow access to Admins or Hotel Owners.
    """
    def has_permission(self, request, view):
        # Allow if user is admin or hotel owner
        return request.user.is_authenticated and (
            request.user.role == 'admin' or request.user.role == 'hotel_owner'
        )

class IsAdminOrCustomer(BasePermission):
    """
    Custom permission to allow access to Admins or Hotel Owners.
    """
    def has_permission(self, request, view):
        # Allow if user is admin or hotel owner
        return request.user.is_authenticated and (
            request.user.role == 'admin' or request.user.role == 'customer'
        )
    
class IsAdminOrDeliveryBoy(BasePermission):
    """
    Custom permission to allow access to Admins or Hotel Owners.
    """
    def has_permission(self, request, view):
        # Allow if user is admin or hotel owner
        return request.user.is_authenticated and (
            request.user.role == 'admin' or request.user.role == 'delivery_boy'
        )