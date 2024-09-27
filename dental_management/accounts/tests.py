from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserViewsTestCase(TestCase):

    def setUp(self):
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')
        self.clinic_url = reverse('clinic')
        self.doctors_url = reverse('doctor')
        self.patients_url = reverse('patients')
        self.username = 'testuser'
        self.email = 'test@example.com'
        self.password = 'password123'

    # Test signup view
    def test_signup_view(self):
        # Strong password for validation
        strong_password = 'Password@123'
        
        # Successful signup
        response = self.client.post(self.signup_url, {
            'username': self.username,
            'email': self.email,
            'password': strong_password
        })
        
        # Check for redirection to login
        self.assertEqual(response.status_code, 302, msg="Signup did not redirect to login.")
        
        # Verify user creation
        user_exists = User.objects.filter(username=self.username).exists()
        self.assertTrue(user_exists, msg="User was not created after signup.")
        
        # Test signup with existing username
        response = self.client.post(self.signup_url, {
            'username': self.username,  # Re-using same username
            'email': 'anotheremail@example.com',
            'password': strong_password
        })
        self.assertEqual(response.status_code, 302)  # Redirect after failed signup

    # Test login view
    def test_login_view(self):
        # Create user for login
        User.objects.create_user(username=self.username, password=self.password, email=self.email)
        
        # Successful login
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Check redirect to home
        self.assertRedirects(response, self.home_url)
        
        # Invalid login
        response = self.client.post(self.login_url, {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)  # Redirect after failed login

    # Test logout view
    def test_logout_view(self):
        # Create user and login
        User.objects.create_user(username=self.username, password=self.password, email=self.email)
        self.client.login(username=self.username, password=self.password)
        
        # Test logout
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Check redirect to login
        self.assertRedirects(response, self.login_url)

    # Test static views (home, clinic, doctors, patients)
    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)  # Home page loads successfully

    def test_clinic_view(self):
        response = self.client.get(self.clinic_url)
        self.assertEqual(response.status_code, 200)  # Clinic page loads successfully

    def test_doctors_view(self):
        response = self.client.get(self.doctors_url)
        self.assertEqual(response.status_code, 200)  # Doctors page loads successfully

    def test_patients_view(self):
        response = self.client.get(self.patients_url)
        self.assertEqual(response.status_code, 200)  # Patients page loads successfully
