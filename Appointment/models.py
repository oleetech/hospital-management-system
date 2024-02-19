from django.db import models
from django.core.exceptions import ValidationError
from Patient.models import Patient
from Doctor.models import Doctor,DoctorAvailability
import calendar


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.patient.name}'s Appointment with Dr. {self.doctor.username}"

        
    def __str__(self):
        return f"{self.patient.name}'s Appointment with Dr. {self.doctor.name}"

    def save(self, *args, **kwargs):
        # Convert appointment date to weekday (Monday=1, Sunday=7)
        appointment_day = self.date.weekday() + 1

        # Check if the doctor is available on this weekday
        doctor_availability = DoctorAvailability.objects.filter(doctor=self.doctor, day_of_week__day=appointment_day)
        if not doctor_availability.exists():
            raise ValidationError("Doctor is not available on this day.")
        
        # Further, check if the appointment time is within the doctor's available hours
        for availability in doctor_availability:
            if self.time < availability.start_time or self.time > availability.end_time:
                raise ValidationError("Doctor is not available at this time.")
        
        super().save(*args, **kwargs)


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField()
    admission_time = models.TimeField()
    discharge_date = models.DateField(null=True, blank=True)
    discharge_time = models.TimeField(null=True, blank=True)
    ward = models.CharField(max_length=100)  # Add more details as necessary
    
    def __str__(self):
        return f"{self.patient.name}'s Visit"