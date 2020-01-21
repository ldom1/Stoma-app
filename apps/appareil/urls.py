from django.urls import path
from . import views

urlpatterns = [
    path('register_appareil/', views.view_register_appareil.as_view(), name='register_appareil'),
    path('appareil/', views.view_display_appareil, name='display_appareil'),
]