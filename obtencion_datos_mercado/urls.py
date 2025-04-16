# obtencion_datos_mercado/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ofertas, name='lista_ofertas'),
    path('extraer_tecnoempleo/', views.extraer_ofertas_tecnoempleo, name='extraer_tecnoempleo'),
    path('extraer_infojobs/', views.extraer_ofertas_infojobs, name='extraer_infojobs'),
    path('extraer_linkedin/', views.extraer_ofertas_linkedin, name='extraer_linkedin'),
]
