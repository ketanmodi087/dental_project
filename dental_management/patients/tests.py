from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Patient
from doctors.models import Doctor, Procedure
from clinics.models import Clinic

class PatientViewSetTests(APITestCase):

    def setUp(self):
        # Create a test doctor and clinic for foreign key relationships
        self.clinic = Clinic.objects.create(
            name="Test Clinic",
            phone="1234567890",
            email="clinic@example.com",
            address="123 Test St"
        )
        
        self.doctor = Doctor.objects.create(
            npi="1234567890",
            name="Dr. Smith",
            specialty="General",
            email="dr.smith@example.com",
            phone="0987654321"
        )

        # Create a test patient
        self.patient = Patient.objects.create(
            name="John Doe",
            address="456 Elm St",
            phone="5551234567",
            date_of_birth="1990-01-01",
            ssn_last_4="1234",
            gender="M",
            last_visit_date="2024-01-01T10:00:00Z",
            last_visit_doctor=self.doctor,
            next_appointment_date="2024-02-01T10:00:00Z",
            next_appointment_doctor=self.doctor,
            clinic=self.clinic
        )
        self.url = reverse('patient-detail', args=[self.patient.id])

    def test_patient_list(self):
        """Test retrieving the list of patients."""
        response = self.client.get(reverse('patient-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming there's only one patient in the database

    def test_patient_detail(self):
        """Test retrieving a patient's detail."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.patient.name)

    def test_create_patient(self):
        """Test creating a new patient."""
        data = {
            'name': "Jane Smith",
            'address': "789 Oak St",
            'phone': "5559876543",
            'date_of_birth': "1995-05-05",
            'ssn_last_4': "5678",
            'gender': "F",
            'last_visit_date': "2024-03-01T10:00:00Z",
            'last_visit_doctor': self.doctor.id,
            'next_appointment_date': "2024-04-01T10:00:00Z",
            'next_appointment_doctor': self.doctor.id,
            'clinic': self.clinic.id
        }
        response = self.client.post(reverse('patient-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 2)  # Check that a new patient has been added

    def test_update_patient(self):
        """Test updating an existing patient."""
        data = {
            'name': "John Doe Updated",
            'address': "456 Elm St",
            'phone': "5551234567",
            'date_of_birth': "1990-01-01",
            'ssn_last_4': "1234",
            'gender': "M",
            'last_visit_date': "2024-01-01T10:00:00Z",
            'last_visit_doctor': self.doctor.id,
            'next_appointment_date': "2024-02-01T10:00:00Z",
            'next_appointment_doctor': self.doctor.id,
            'clinic': self.clinic.id
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.name, "John Doe Updated")

    def test_delete_patient(self):
        """Test deleting a patient."""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 0)  # Check that the patient has been deleted
