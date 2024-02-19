from django.db import models
from django.core.exceptions import ValidationError
from Patient.models import Patient
from Doctor.models import Doctor,DoctorAvailability

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.patient.name}'s Appointment with Dr. {self.doctor.username}"

        
    def save(self, *args, **kwargs):
        # Check if there is DoctorAvailability for the doctor on the appointment date
        try:
            doctor_availability = DoctorAvailability.objects.get(
                doctor=self.doctor,
                day_of_week=self.date.weekday() + 1  # Monday=1, Sunday=7
            )
            if self.time < doctor_availability.start_time or self.time > doctor_availability.end_time:
                raise ValidationError("Doctor is not available at this time.")
        except DoctorAvailability.DoesNotExist:
            raise ValidationError("Doctor is not available on this day.")

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