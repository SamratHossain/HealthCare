from django.urls import path
from . import views

urlpatterns = [
    path('add-experience/', views.AddExperience, name="AddExperience")
]
