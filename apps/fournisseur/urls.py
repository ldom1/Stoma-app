from django.urls import path
from . import views

urlpatterns = [
    path('register_fournisseur/', views.view_register_fournisseur.as_view(), name='register_fournisseur'),
    path('fournisseur/', views.view_display_fournisseur, name='display_fournisseur'),
]