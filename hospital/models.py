# patient_management/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='')
    experience_years = models.PositiveIntegerField(default=0)
    specialization = models.CharField(max_length=100)
    qualifications = models.TextField()
    departments = models.ManyToManyField(Department, related_name='doctors')
    def __str__(self):
        return self.user.username
    
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    medical_history = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.patient.name}'s Appointment with Dr. {self.doctor.name}"

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
    

class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[(i, i) for i in range(1, 8)])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.day_of_week} - {self.start_time} to {self.end_time}"    
