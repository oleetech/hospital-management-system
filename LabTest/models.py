from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from Patient.models import Patient


class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Lab(models.Model):
    name = models.CharField(max_length=100)
    # Add other details about the lab like location, contact info, etc.

    def __str__(self):
        return self.name

class TestSchedule(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Test Schedule for {self.patient} - {self.test} at {self.lab} on {self.scheduled_date}"

class TestResult(models.Model):
    test_schedule = models.OneToOneField(TestSchedule, on_delete=models.CASCADE)
    result = models.TextField()

    def __str__(self):
        return f"Test Result for {self.test_schedule}"

@receiver(post_save, sender=TestResult)
def update_test_schedule(sender, instance, created, **kwargs):
    if created:
        instance.test_schedule.is_completed = True
        instance.test_schedule.save()

