from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Check for Fundraiser owner or Pledge supporter
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        elif hasattr(obj, 'supporter'):
            return obj.supporter == request.user
        return False
        # else:
        #     return obj.owner == request.user


# class IsSupporterOrReadOnly

# class CustomPermission(permissions.BasePermission):
#             message = 'You do not have the necessary permissions to perform this action.'

#             def has_permission(self, request, view):
#                 # Your permission logic here
#                 return False # Example: always deny for demonstration