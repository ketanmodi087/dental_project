from django.urls import path
from .views import signup_view, login_view, logout_view ,doctors_view
from . import views
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', views.home_view, name='home'),
    path('clinic/', views.clinic_view, name='clinic'),
    path('patients/', views.patients_view, name='patients'),
    path('doctors/',views.doctors_view,name='doctor')  # Home view for the root URL
]

