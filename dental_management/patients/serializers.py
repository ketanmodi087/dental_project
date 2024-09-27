from rest_framework import serializers
from .models import Patient, Visit, Appointment
from doctors.models import Doctor, Procedure
from clinics.models import Clinic

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['id', 'name']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'npi', 'name', 'specialty', 'email', 'phone']

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'name', 'phone', 'email', 'address']

class VisitSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    clinic = ClinicSerializer(read_only=True)  # Assuming you want detailed clinic info
    procedures_done = ProcedureSerializer(many=True, read_only=True)

    class Meta:
        model = Visit
        fields = ['id', 'visit_date', 'doctor', 'clinic', 'procedures_done', 'notes']

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = serializers.StringRelatedField(read_only=True)  # Assuming Patient has a __str__ method
    procedures = ProcedureSerializer(many=True, read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'appointment_date', 'doctor', 'patient', 'procedures', 'status', 'notes']

class PatientSerializer(serializers.ModelSerializer):
    last_visit_doctor = DoctorSerializer(read_only=True)
    next_appointment_doctor = DoctorSerializer(read_only=True)
    last_visit_procedures = ProcedureSerializer(many=True, read_only=True)
    next_appointment_procedures = ProcedureSerializer(many=True, read_only=True)
    visits = VisitSerializer(many=True, read_only=True) 
    appointments = AppointmentSerializer(many=True, read_only=True)  
    clinic = ClinicSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id', 'name', 'address', 'phone', 'date_of_birth', 
            'ssn_last_4', 'gender', 'last_visit_date', 
            'last_visit_doctor', 'last_visit_procedures',
            'next_appointment_date', 'next_appointment_doctor', 
            'next_appointment_procedures', 'clinic', 'visits', 
            'appointments'
        ]
