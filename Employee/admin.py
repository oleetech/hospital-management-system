from django.contrib import admin
from .models import Employee, Shift, Attendance, Performance

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'is_doctor', 'is_nurse')  # Add other fields if needed
    search_fields = ['user__username', 'department__name']  # Add fields you want to search by
    list_filter = ['department', 'is_doctor', 'is_nurse']  # Add filters you want to apply

admin.site.register(Employee, EmployeeAdmin)

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')  # Add other fields if needed
    search_fields = ['name']  # Add fields you want to search by

admin.site.register(Shift, ShiftAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'shift', 'date', 'is_present')
    search_fields = ['employee__user__username']  # Add fields you want to search by
    list_filter = ['shift', 'date', 'is_present']  # Add filters you want to apply

admin.site.register(Attendance, AttendanceAdmin)

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'rating')
    search_fields = ['employee__user__username']  # Add fields you want to search by
    list_filter = ['date']  # Add filters you want to apply

admin.site.register(Performance, PerformanceAdmin)
