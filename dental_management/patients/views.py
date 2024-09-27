from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import viewsets
from .models import  Patient
from .serializers import PatientSerializer

import requests

# from django.views.generic import TemplateView

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# View to render the initial patient detail page
def patient_detail_page(request):
    patients = Patient.objects.all()
    context = {
        "patient": patients
    }
    return render(request, 'patient_detail.html', context=context)

# views.py
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

class PatientDetailView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'id'  # This ensures it looks for 'id' instead of 'pk'
