from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'gender', 'contact_number', 'email')
    search_fields = ['name', 'address', 'contact_number']  # Add fields you want to search by
    list_filter = ['gender', 'date_of_birth']  # Add filters you want to apply

admin.site.register(Patient, PatientAdmin)

