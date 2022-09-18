from django.urls import path
from . import views

urlpatterns = [
    path('view-category/', views.ViewCategory, name="ViewCategory"),
    path('search-category/<str:name>', views.SearchCategory, name="SearchCategory"),
    path('doctor-list/', views.DoctorListInformation, name="DoctorListInfo"),
    path('view-experience/', views.ViewExperience, name="ViewExperience"),
    path('getreview/', views.getReview, name="GetReview"),
    path('doctorlisttest/', views.DoctorListInformationTest, name="GetReview"),
]