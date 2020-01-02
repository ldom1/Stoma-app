from django.urls import path
from . import views

urlpatterns = [
    path('register_collaborateur/', views.view_register_collaborateur.as_view(), name='register_collaborateur'),
    path('collaborateurs/', views.view_display_collaborateur, name='display_collaborateur'),
]