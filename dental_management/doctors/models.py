import datetime
from django.db import models
from clinics.models import Clinic
from patients.models import Appointment  # Make sure to import Appointment

class Procedure(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models

class Doctor(models.Model):
    npi = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    affiliated_clinics = models.ManyToManyField('clinics.Clinic', related_name='doctors_clinic')  # Use string reference
    offered_procedures = models.ManyToManyField('Procedure')
    patients = models.ManyToManyField('patients.Patient', related_name='doctors', blank=True)  # Use string reference

    def __str__(self):
        return self.name

class DoctorAffiliation(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='affiliations', on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, related_name='affiliations', on_delete=models.CASCADE)
    office_address = models.CharField(max_length=255)
    working_days = models.CharField(max_length=100)  # Example: "Mon-Fri"
    working_hours_start = models.TimeField()
    working_hours_end = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} at {self.clinic.name}"