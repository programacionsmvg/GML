# obtencion_datos_mercado/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ofertas, name='lista_ofertas'),
    # TODO: Añadir URLs para web scraping e importación de datos
]