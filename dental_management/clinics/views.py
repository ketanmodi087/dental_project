from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Clinic
from .serializers import ClinicSerializer

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

