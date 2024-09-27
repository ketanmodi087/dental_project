# urls.py

from django.urls import path
from .views import  PatientDetailView, PatientViewSet,patient_detail_page
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('patients', PatientViewSet)


urlpatterns = [
    path('patientdetail/', patient_detail_page, name='patientdetail'),
    path('patientsor/<int:id>/', PatientDetailView.as_view(), name='patient-detail'),  # ensure this matches your AJAX URL
] + router.urls
