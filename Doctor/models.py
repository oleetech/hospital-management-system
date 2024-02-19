from django.db import models
from django.contrib.auth.models import User
from General.models import Department

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]



    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    qualifications = models.TextField()
    departments = models.ManyToManyField(Department, related_name='doctors')

    def __str__(self):
        return self.name

class Nurse(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    # Add other fields specific to nurses as needed

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username


# Model to represent days of the week
class WeekDay(models.Model):
    DAY_CHOICES = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]
    day = models.IntegerField(choices=DAY_CHOICES, unique=True)

    def __str__(self):
        return self.get_day_display()

class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.ManyToManyField(WeekDay, related_name='doctor_availabilities')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.day_of_week} - {self.start_time} to {self.end_time}"
