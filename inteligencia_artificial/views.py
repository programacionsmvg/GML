# inteligencia_artificial/views.py
from django.shortcuts import render
from .models import Recomendacion  # Asegúrate de importar tus modelos

def recomendaciones(request):
    recomendaciones_lista = Recomendacion.objects.all()  # Obtén las recomendaciones de la base de datos
    return render(request, 'inteligencia_artificial/recomendaciones.html', {'recomendaciones': recomendaciones_lista})

def predicciones(request):
    # Aquí iría la lógica para obtener las predicciones
    predicciones_data = {
        'habilidades_futuras': ['Python', 'Machine Learning', 'Big Data'],
        'tendencias_futuras': ['Aumento en la demanda de IA', 'Automatización de procesos']
    }
    return render(request, 'inteligencia_artificial/predicciones.html', {'predicciones': predicciones_data})