# urls.py

from django.urls import path
from .views import generate_patient_report, appointment_report, visit_report

urlpatterns = [
    path('patient/<int:patient_id>/report/', generate_patient_report, name='patient_report'),
    path('appointment/report/', appointment_report, name='appointment_report'),
    path('visit/report/', visit_report, name='visit_report'),
]

