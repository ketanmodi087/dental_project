from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField()
    ssn_last_4 = models.CharField(max_length=4, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    
    last_visit_date = models.DateTimeField(null=True, blank=True)
    last_visit_doctor = models.ForeignKey('doctors.Doctor', related_name='last_visits', null=True, blank=True, on_delete=models.SET_NULL)
    last_visit_procedures = models.ManyToManyField('doctors.Procedure', related_name='last_visit_patients', blank=True)
    
    next_appointment_date = models.DateTimeField(null=True, blank=True)
    next_appointment_doctor = models.ForeignKey('doctors.Doctor', related_name='next_appointments', null=True, blank=True, on_delete=models.SET_NULL)
    next_appointment_procedures = models.ManyToManyField('doctors.Procedure', related_name='next_appointment_patients', blank=True)
    
    clinic = models.ForeignKey('clinics.Clinic', related_name='patients_list', null=True, blank=True, on_delete=models.SET_NULL)  # Ensure unique related_name

    def __str__(self):
        return self.name

class Visit(models.Model):
    patient = models.ForeignKey('Patient', related_name='visits', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', related_name='visits', on_delete=models.CASCADE)
    clinic = models.ForeignKey('clinics.Clinic', related_name='visits', on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    procedures_done = models.ManyToManyField('doctors.Procedure', related_name='visits', blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Visit for {self.patient.name} with {self.doctor.name} on {self.visit_date}"


class Appointment(models.Model):
    patient = models.ForeignKey('Patient', related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', related_name='appointments', on_delete=models.CASCADE)
    procedures = models.ManyToManyField('doctors.Procedure', related_name='appointments', blank=True)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Appointment for {self.patient.name} with {self.doctor.name} on {self.appointment_date}"

    
