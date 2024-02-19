from rest_framework import permissions

class HasPatientPermission(permissions.BasePermission):
    """
    Custom permission to only allow users with the appropriate patient permissions.
    """

    def has_permission(self, request, view):
        # Check permissions for read-only requests
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('Patient.view_patient')
        # Check permissions for write requests
        elif request.method == 'POST':
            return request.user.has_perm('Patient.add_patient')
        elif request.method in 'PUT' or request.method == 'PATCH':
            return request.user.has_perm('Patient.change_patient')
        elif request.method == 'DELETE':
            return request.user.has_perm('Patient.delete_patient')
        return False

    def has_object_permission(self, request, view, obj):
        # Check permissions for object-level requests
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('Patient.view_patient', obj)
        elif request.method == 'PUT' or request.method == 'PATCH':
            return request.user.has_perm('Patient.change_patient', obj)
        elif request.method == 'DELETE':
            return request.user.has_perm('Patient.delete_patient', obj)
        return False
