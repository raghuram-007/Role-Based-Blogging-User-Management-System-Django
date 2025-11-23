from django.urls import path
from .views import*

urlpatterns = [
    path('',SignupView , name='signup'),
     path('login/', login_view, name='login'),
     path('logout/', logout_view, name='logout'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
]
