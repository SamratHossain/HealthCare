from django.urls  import path
from . import views

urlpatterns = [
    path('send-message/', views.SendMessage, name="SendMessage")
]