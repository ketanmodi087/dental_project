from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clinics/', include('clinics.urls')),   # Clinics app URLs
    path('api/doctors/', include('doctors.urls')),   # Doctors app URLs
    path('api/patients/', include('patients.urls')), # Patients app URLs
    path('', include('accounts.urls')),
]
