from django.urls import path
from . import views

urlpatterns = [
    path('register_controle_reception/', views.view_register_controle_reception.as_view(), name='register_controle_reception'),
]