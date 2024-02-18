# patient_management/admin.py

from django.contrib import admin
from .models import Patient, Appointment, Visit,Doctor



@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    change_form_template = 'change_form.html'  
    class Media:           
        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css'),
        } 

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    change_form_template = 'change_form.html'  
    class Media:           
        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css'),
        }  

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'time', 'reason', 'is_completed']
    list_filter = ['doctor', 'date', 'is_completed']
    search_fields = ['patient__name', 'reason']
    date_hierarchy = 'date'
    change_form_template = 'change_form.html'  
    class Media:           
        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css'),
        }     

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['patient', 'admission_date', 'admission_time', 'discharge_date', 'discharge_time', 'ward']
    list_filter = ['admission_date', 'ward']
    search_fields = ['patient__name']
    date_hierarchy = 'admission_date'

    change_form_template = 'change_form.html'  
    class Media:           
        css = {
            'all': ('css/bootstrap.min.css','css/admin_styles.css'),
        } 
