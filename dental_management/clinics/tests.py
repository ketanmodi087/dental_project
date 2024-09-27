from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Clinic

class ClinicViewSetTestCase(APITestCase):

    def setUp(self):
        self.clinic_data = {
            'name': 'Test Clinic',
            'address': '123 Test St, Test City',
            'phone': '123-456-7890',
            'email': 'test@clinic.com',  # Added email
            'city': 'Test City',          # Added city
            'state': 'Test State'         # Added state
        }
        self.clinic = Clinic.objects.create(**self.clinic_data)
        self.clinic_url = reverse('clinic-list')  # Assuming 'clinic-list' is the URL for the list view

    # Test creating a clinic
    def test_create_clinic(self):
        response = self.client.post(self.clinic_url, self.clinic_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Clinic.objects.count(), 2)  # One existing + one created

    # Test retrieving a list of clinics
    def test_get_clinics(self):
        response = self.client.get(self.clinic_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one clinic should exist

    # Test retrieving a single clinic
    def test_get_clinic(self):
        response = self.client.get(reverse('clinic-detail', args=[self.clinic.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.clinic_data['name'])

    # Test updating a clinic
    def test_update_clinic(self):
        updated_data = {
            'name': 'Updated Clinic',
            'address': '456 Updated St, Updated City',
            'phone': '987-654-3210',
            'email': 'updated@clinic.com',  # Ensure to keep all fields
            'city': 'Updated City',
            'state': 'Updated State'
        }
        response = self.client.put(reverse('clinic-detail', args=[self.clinic.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.clinic.refresh_from_db()
        self.assertEqual(self.clinic.name, updated_data['name'])

    # Test deleting a clinic
    def test_delete_clinic(self):
        response = self.client.delete(reverse('clinic-detail', args=[self.clinic.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Clinic.objects.count(), 0)  # The clinic should be deleted
