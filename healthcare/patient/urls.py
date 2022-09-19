from django.urls import path
from . import views

urlpatterns = [
    path('view-category/', views.ViewCategory, name="ViewCategory"),
    path('search-category/<str:name>', views.SearchCategory, name="SearchCategory"),
    path('doctor-list/', views.DoctorListInformation, name="DoctorListInfo"),
    path('view-experience/<int:id>', views.ViewExperience, name="ViewExperience"),
    path('view-doctorinfo/<int:id>', views.ViewDoctorInfo, name="ViewExperience"),
    path('view-doctor/<int:id>', views.ViewDoctor, name="ViewExperience"),
    path('view-qualification/<int:id>', views.ViewQualification, name="ViewQualification"),
    path('getreview/', views.getReview, name="GetReview"),
    path('doctorlisttest/', views.DoctorListInformationTest, name="GetReview"),
]