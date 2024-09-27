from django.contrib import admin
from .models import Clinic

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'city', 'state')
    filter_horizontal = ('doctors', 'patients')  # To show M2M fields nicely

