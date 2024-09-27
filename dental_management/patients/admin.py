from django.contrib import admin
from .models import Patient, Visit, Appointment  # Assuming you also want to register Visit and Appointment

class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date_of_birth',
        'last_visit_date',
        'last_visit_doctor',
        'next_appointment_date',
        'next_appointment_doctor',
    )
    search_fields = ('name', 'ssn_last_4')
    list_filter = ('last_visit_doctor', 'next_appointment_doctor')
    filter_horizontal = ('last_visit_procedures', 'next_appointment_procedures')

admin.site.register(Patient, PatientAdmin)

# Register Visit and Appointment if needed
admin.site.register(Visit)
admin.site.register(Appointment)
