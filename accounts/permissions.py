from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role=='admin'
class IsHotelOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role=='hotel_owner'
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role=='customer'
class IsDeliveryBoy(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role=='delivery_boy'
    