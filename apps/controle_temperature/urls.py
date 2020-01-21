from django.urls import path
from . import views

urlpatterns = [
    path('register_controle_temperature/', views.view_register_controle_temperature.as_view(), name='register_controle_temperature'),
]