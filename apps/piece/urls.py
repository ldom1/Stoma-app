from django.urls import path
from . import views

urlpatterns = [
    path('register_piece/', views.view_register_piece.as_view(), name='register_piece'),
    path('piece/', views.view_display_piece, name='display_piece'),
]