from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('student/', views.StudentApi)
# router.register('mark/', views.MarksApi)

urlpatterns = [
    path('view-category/', views.ViewCategory, name="SearchCategory"),
    path('search-category/<str:name>', views.SearchCategory, name="SearchCategory"),
    path('student/', views.StudentApi, name="SearchCategory"),
    path('mark/', views.MarksApi, name="SearchCategory"),
]