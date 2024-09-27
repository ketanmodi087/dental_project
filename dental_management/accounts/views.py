from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

def home_view(request):
    return render(request, 'home.html')

def clinic_view(request):
    return render(request, 'clinic.html')

def doctors_view(request):
    return render(request, 'doctors.html')

def patients_view(request):
    return render(request, 'patient.html')

def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            return redirect('signup')

        try:
            validate_password(password)
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('login')
        except ValidationError as e:
            # Instead of redirecting, you can pass the error messages to the signup form
            return redirect('signup')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Successful login, redirect to home
        else:
            return redirect('login')  # Invalid credentials, just redirect
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Logout successful, redirect to login
