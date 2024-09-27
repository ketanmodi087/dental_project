from rest_framework import serializers
from doctors.models import Doctor, Procedure, DoctorAffiliation
from clinics.models import Clinic
from patients.models import Patient

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['id', 'name']

class DoctorAffiliationSerializer(serializers.ModelSerializer):
    clinic = serializers.StringRelatedField(read_only=True)  # Show the clinic name
    
    class Meta:
        model = DoctorAffiliation
        fields = ['clinic', 'office_address', 'working_days', 'working_hours_start', 'working_hours_end']

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'name', 'phone', 'email', 'address', 'city', 'state']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'phone']

class DoctorSerializer(serializers.ModelSerializer):
    affiliated_clinics = ClinicSerializer(many=True, read_only=True)  # Show the affiliated clinics
    offered_procedures = ProcedureSerializer(many=True, read_only=True)
    affiliations = DoctorAffiliationSerializer(many=True, read_only=True)  # Show affiliations
    patients = PatientSerializer(many=True, read_only=True)  # Show related patients

    class Meta:
        model = Doctor
        fields = [
            'id', 'npi', 'name', 'specialty', 'email', 'phone',
            'affiliated_clinics', 'offered_procedures', 'affiliations', 'patients'
        ]
