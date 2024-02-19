
from django.contrib import admin
from .models import Doctor, DoctorAvailability

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'contact_number', 'email', 'specialization', 'qualifications')
    search_fields = ['name', 'specialization']  # Add fields you want to search by

class DoctorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_week', 'start_time', 'end_time')
    list_filter = ['day_of_week']  # Add filters you want to apply

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(DoctorAvailability, DoctorAvailabilityAdmin)
