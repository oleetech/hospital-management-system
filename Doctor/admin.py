
from django.contrib import admin
from .models import Doctor, DoctorAvailability,Nurse,WeekDay

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'contact_number', 'specialization', 'qualifications')
    search_fields = ['name', 'specialization']  # Add fields you want to search by

class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')
    search_fields = ['name' ]  

class DoctorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'get_days_of_week', 'start_time', 'end_time')

    def get_days_of_week(self, obj):
        return ", ".join([day.get_day_display() for day in obj.day_of_week.all()])
    get_days_of_week.short_description = 'Days of the Week'

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(DoctorAvailability, DoctorAvailabilityAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(WeekDay)