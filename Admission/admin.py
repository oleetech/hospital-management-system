from django.contrib import admin
from .models import Admission

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'ward', 'room', 'bed', 'admission_date', 'discharge_date', 'is_discharged')
    search_fields = ['patient__name', 'ward__name']  # Add fields you want to search by
    list_filter = ['ward', 'is_discharged', 'admission_date', 'discharge_date']  # Add filters you want to apply

admin.site.register(Admission, AdmissionAdmin)

