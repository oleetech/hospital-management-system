from django.contrib import admin
from .models import Appointment, Visit

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'reason', 'is_completed')
    search_fields = ['patient__name', 'doctor__username', 'reason']  # Add fields you want to search by
    list_filter = ['date', 'is_completed']  # Add filters you want to apply

admin.site.register(Appointment, AppointmentAdmin)

class VisitAdmin(admin.ModelAdmin):
    list_display = ('patient', 'admission_date', 'admission_time', 'discharge_date', 'discharge_time', 'ward')
    search_fields = ['patient__name', 'ward']  # Add fields you want to search by
    list_filter = ['admission_date', 'ward']  # Add filters you want to apply

admin.site.register(Visit, VisitAdmin)

