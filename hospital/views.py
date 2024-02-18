


# views.py
from django.shortcuts import render
from .models import Patient, Appointment, Visit

def generate_patient_report(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
        appointments = Appointment.objects.filter(patient=patient)
        visits = Visit.objects.filter(patient=patient)
        
        context = {
            'patient': patient,
            'appointments': appointments,
            'visits': visits,
        }
        
        return render(request, 'patient/patient_report.html', context)
    except Patient.DoesNotExist:
        # Handle case where patient does not exist
        return render(request, 'patient/patient_not_found.html')


def appointment_report(request):
    appointments = Appointment.objects.all()
    return render(request, 'patient/appointment_report.html', {'appointments': appointments})

def visit_report(request):
    visits = Visit.objects.all()
    return render(request, 'patient/visit_report.html', {'visits': visits})