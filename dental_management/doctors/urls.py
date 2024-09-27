from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, ProcedureViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)     
router.register('procedures', ProcedureViewSet)  

urlpatterns = ([]+router.urls)