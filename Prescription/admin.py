from django.contrib import admin
from .models import Medication, Prescription, PrescribedMedication, MedicationHistory

class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Add other fields if needed
    search_fields = ['name']  # Add fields you want to search by

admin.site.register(Medication, MedicationAdmin)

class PrescribedMedicationInline(admin.TabularInline):
    model = PrescribedMedication
    extra = 1

class MedicationHistoryInline(admin.TabularInline):
    model = MedicationHistory
    extra = 1

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_prescribed')
    search_fields = ['patient__name']  # Add fields you want to search by
    inlines = [PrescribedMedicationInline]

admin.site.register(Prescription, PrescriptionAdmin)

class PrescribedMedicationAdmin(admin.ModelAdmin):
    list_display = ('prescription', 'medication', 'dosage', 'refills_remaining')
    search_fields = ['prescription__patient__name', 'medication__name']  # Add fields you want to search by

admin.site.register(PrescribedMedication, PrescribedMedicationAdmin)

class MedicationHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medication', 'date', 'dosage', 'refills_taken')
    search_fields = ['patient__name', 'medication__name']  # Add fields you want to search by

admin.site.register(MedicationHistory, MedicationHistoryAdmin)

