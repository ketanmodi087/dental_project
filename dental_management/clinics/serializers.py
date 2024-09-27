from rest_framework import serializers
from clinics.models import Clinic
from doctors.models import Doctor
from patients.models import Patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'email', 'phone']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'last_visit_date', 'next_appointment_date']

class ClinicSerializer(serializers.ModelSerializer):
    doctors = serializers.PrimaryKeyRelatedField(many=True, queryset=Doctor.objects.all())
    patients = serializers.PrimaryKeyRelatedField(many=True, queryset=Patient.objects.all())

    class Meta:
        model = Clinic
        fields = ['id', 'name', 'phone', 'email', 'address', 'city', 'state', 'doctors', 'patients']
