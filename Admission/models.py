from django.db import models
from Patient.models import Patient
from General.models import Bed,Ward,Room
class Admission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.SET_NULL,null=True,blank=True)
    bed = models.ForeignKey(Bed, on_delete=models.SET_NULL, null=True, blank=True)
    admission_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField(null=True, blank=True)
    reason = models.TextField()
    is_discharged = models.BooleanField(default=False)

    def __str__(self):
        return f"Admission of {self.patient} in {self.ward} on {self.admission_date}"
