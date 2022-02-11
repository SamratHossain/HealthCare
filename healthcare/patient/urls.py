from django.urls import path
from . import views

urlpatterns = [
    path('view-category/', views.ViewCategory, name="SearchCategory"),
    path('search-category/<str:name>', views.SearchCategory, name="SearchCategory"),
]