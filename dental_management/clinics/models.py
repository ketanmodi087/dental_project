# clinics/models.py
from django.db import models

# from doctors.models import Doctor
# from patients.models import Patient

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    doctors = models.ManyToManyField('doctors.Doctor', blank=True)
    patients = models.ManyToManyField('patients.Patient', blank=True, related_name='clinics')  # Ensure unique related_name

    def __str__(self):
        return self.name
