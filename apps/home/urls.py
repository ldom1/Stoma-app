from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('administration/', views.view_admin, name='admin'),
]
