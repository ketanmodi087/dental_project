from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Doctor, Procedure
from .serializers import DoctorSerializer, ProcedureSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
