from rest_framework import permissions

class HasAppointmentPermission(permissions.BasePermission):
    """
    Custom permission to only allow users with the appropriate appointment permissions.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('Appointment.view_appointment')
        elif request.method == 'POST':
            return request.user.has_perm('Appointment.add_appointment')
        elif request.method in 'PUT' or request.method == 'PATCH':
            return request.user.has_perm('Appointment.change_appointment')
        elif request.method == 'DELETE':
            return request.user.has_perm('Appointment.delete_appointment')
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
