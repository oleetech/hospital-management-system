from django.db import models
from django.contrib.auth.models import User
from General.models import Department


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    # Add other employee details like contact info, etc.

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username

class Shift(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} attendance on {self.date}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    rating = models.PositiveIntegerField(default=0)
    comment = models.TextField()

    def __str__(self):
        return f"Performance of {self.employee} on {self.date}"
