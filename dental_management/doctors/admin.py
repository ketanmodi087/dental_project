from django.contrib import admin
from .models import Doctor, Procedure

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['npi', 'name', 'specialty', 'email', 'phone']
    search_fields = ['name', 'specialty', 'npi']
    filter_horizontal = ['affiliated_clinics', 'offered_procedures']

@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
 