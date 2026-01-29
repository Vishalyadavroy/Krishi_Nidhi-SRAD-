from rest_framework.permissions import BasePermission, SAFE_METHODS


class BaseRolePermission(BasePermission):
    """
    Base permission for role-based access.
    Child classes must define `allowed_roles`.
    """
    allowed_roles = []

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role in self.allowed_roles
        )


class IsAdmin(BaseRolePermission):
    allowed_roles = ['ADMIN']


class IsCompany(BaseRolePermission):
    allowed_roles = ['COMPANY']


class IsWholesaler(BaseRolePermission):
    allowed_roles = ['WHOLESALER']


class IsRetailer(BaseRolePermission):
    allowed_roles = ['RETAILER']


class IsFarmer(BaseRolePermission):
    allowed_roles = ['FARMER']


class IsSeller(BaseRolePermission):
    allowed_roles = ['COMPANY', 'WHOLESALER', 'RETAILER']


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.created_by == request.user
