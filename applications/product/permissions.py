from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomIsAdmin(BasePermission):
    # CREATE, LIST
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated and request.user.is_staff

    # UPDATE , DELETE, RETRIEVE
    def has_object_permission(self, request, view, obj):
        # print(SAFE_METHODS)
        # print(obj)
        # print(request.user)
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff
