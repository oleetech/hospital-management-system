from django.db import models

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
    email = models.EmailField(default='',null=True,blank=True)
    medical_history = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
