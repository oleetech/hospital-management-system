from django.db import models
from Patient.models import Patient

class Medication(models.Model):
    name = models.CharField(max_length=100)
    # Add other details about the medication like dosage, etc.

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medications = models.ManyToManyField(Medication, through='PrescribedMedication')
    instructions = models.TextField()
    date_prescribed = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.name} on {self.date_prescribed}"

class PrescribedMedication(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    refills_remaining = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.medication.name} - {self.dosage} - Refills: {self.refills_remaining}"

class MedicationHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    date = models.DateField()
    dosage = models.CharField(max_length=100)
    refills_taken = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.patient.name}'s {self.medication.name} - {self.dosage} - Refills Taken: {self.refills_taken}"
