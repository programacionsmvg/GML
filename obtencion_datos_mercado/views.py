# obtencion_datos_mercado/views.py
from django.shortcuts import render
from .models import OfertaEmpleo

def lista_ofertas(request):
    ofertas = OfertaEmpleo.objects.all()
    return render(request, 'obtencion_datos_mercado/lista_ofertas.html', {'ofertas': ofertas})

# TODO: Implementar vistas para web scraping e importación de datos