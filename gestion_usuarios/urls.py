# gestion_usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    # TODO: Añadir URLs para inicio de sesión y gestión de usuarios
]