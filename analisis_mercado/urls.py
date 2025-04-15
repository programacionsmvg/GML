# analisis_mercado/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.analisis_principal, name='analisis_principal'),
    path('tendencias/', views.tendencias_mercado, name='tendencias_mercado'),
    path('habilidades/', views.habilidades_demandadas, name='habilidades_demandadas'),
    path('regiones/', views.tendencias_regiones, name='tendencias_regiones'),
    path('industrias/', views.tendencias_industrias, name='tendencias_industrias'),
]