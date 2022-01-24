from django.urls import path
from . import views

urlpatterns = [
    path('add-experience/', views.AddExperience, name="AddExperience"),
    path('view-experience/', views.ViewExperience, name="ViewExperience"),
    path('view-qualification/', views.ViewQualification, name="ViewQualification"),
    path('view-doctor-info/', views.ViewDoctorInfo, name="ViewDoctorInfo"),
    path('view-personal-info/', views.ViewPersonalInfo, name="ViewPersonalInfo")
]
