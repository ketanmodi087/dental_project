# doctors/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Doctor, Procedure, Clinic

class DoctorViewSetTestCase(APITestCase):
    def setUp(self):
        self.clinic = Clinic.objects.create(
            name='Test Clinic',
            phone='123-456-7890',
            email='test@clinic.com',
            address='123 Test St, Test City',
            city='Test City',
            state='Test State'
        )
        self.doctor_data = {
            'npi': '1234567890',
            'name': 'Test Doctor',
            'specialty': 'Cardiology',
            'email': 'doctor@test.com',
            'phone': '123-456-7890'
        }
        self.doctor_url = reverse('doctor-list')  # Assuming 'doctor-list' is the URL for the list view

    # Test creating a doctor
    def test_create_doctor(self):
        response = self.client.post(self.doctor_url, self.doctor_data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 1)

    # Test retrieving a list of doctors
    def test_get_doctors(self):
        Doctor.objects.create(**self.doctor_data)
        response = self.client.get(self.doctor_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test retrieving a single doctor
    def test_get_doctor(self):
        doctor = Doctor.objects.create(**self.doctor_data)
        response = self.client.get(reverse('doctor-detail', args=[doctor.id]))  # Assuming 'doctor-detail' URL is set correctly
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.doctor_data['name'])

    # Test updating a doctor
    def test_update_doctor(self):
        doctor = Doctor.objects.create(**self.doctor_data)
        updated_data = {
            'npi': '0987654321',
            'name': 'Updated Doctor',
            'specialty': 'Dermatology',
            'email': 'updated_doctor@test.com',
            'phone': '987-654-3210'
        }
        response = self.client.put(reverse('doctor-detail', args=[doctor.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        doctor.refresh_from_db()
        self.assertEqual(doctor.name, updated_data['name'])

    # Test deleting a doctor
    def test_delete_doctor(self):
        doctor = Doctor.objects.create(**self.doctor_data)
        response = self.client.delete(reverse('doctor-detail', args=[doctor.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Doctor.objects.count(), 0)


class ProcedureViewSetTestCase(APITestCase):
    def setUp(self):
        self.procedure_data = {
            'name': 'Test Procedure'
        }
        self.procedure_url = reverse('procedure-list')  # Assuming 'procedure-list' is the URL for the list view

    # Test creating a procedure
    def test_create_procedure(self):
        response = self.client.post(self.procedure_url, self.procedure_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Procedure.objects.count(), 1)

    # Test retrieving a list of procedures
    def test_get_procedures(self):
        Procedure.objects.create(**self.procedure_data)
        response = self.client.get(self.procedure_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test retrieving a single procedure
    def test_get_procedure(self):
        procedure = Procedure.objects.create(**self.procedure_data)
        response = self.client.get(reverse('procedure-detail', args=[procedure.id]))  # Assuming 'procedure-detail' URL is set correctly
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.procedure_data['name'])

    # Test updating a procedure
    def test_update_procedure(self):
        procedure = Procedure.objects.create(**self.procedure_data)
        updated_data = {
            'name': 'Updated Procedure'
        }
        response = self.client.put(reverse('procedure-detail', args=[procedure.id]), updated_data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        procedure.refresh_from_db()
        self.assertEqual(procedure.name, updated_data['name'])

    # Test deleting a procedure
    def test_delete_procedure(self):
        procedure = Procedure.objects.create(**self.procedure_data)
        response = self.client.delete(reverse('procedure-detail', args=[procedure.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Procedure.objects.count(), 0)
