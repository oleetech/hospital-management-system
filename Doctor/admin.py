
from django.contrib import admin
from .models import Doctor, DoctorAvailability,Nurse

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'contact_number', 'specialization', 'qualifications')
    search_fields = ['name', 'specialization']  # Add fields you want to search by

class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')
    search_fields = ['name' ]  

class DoctorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_week', 'start_time', 'end_time')
    list_filter = ['day_of_week']  # Add filters you want to apply

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(DoctorAvailability, DoctorAvailabilityAdmin)
admin.site.register(Nurse, NurseAdmin)