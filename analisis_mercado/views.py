from django.shortcuts import render
from .models import DatoMercado
from obtencion_datos_mercado.models import OfertaHabilidad, OfertaEmpleo  # Importar modelos necesarios
from django.db.models import Count
import matplotlib.pyplot as plt
import io
import base64

def analisis_principal(request):
    return render(request, 'analisis_mercado/analisis_principal.html')

def tendencias_mercado(request):
    datos = DatoMercado.objects.all().order_by('fecha')
    fechas = [dato.fecha.strftime('%Y-%m-%d') for dato in datos]
    cantidad_ofertas = [dato.ofertas.count() for dato in datos]  # Verifica si esta relación existe en el modelo

    plt.figure(figsize=(10, 5))
    plt.plot(fechas, cantidad_ofertas)
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad de Ofertas')
    plt.title('Tendencias del Mercado Laboral')
    plt.xticks(rotation=45)
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'analisis_mercado/tendencias_mercado.html', {'graphic': graphic})

def habilidades_demandadas(request):
    habilidades = OfertaHabilidad.objects.values('habilidad__nombre').annotate(cantidad=Count('habilidad')).order_by('-cantidad')
    return render(request, 'analisis_mercado/habilidades_demandadas.html', {'habilidades': habilidades})

def tendencias_regiones(request):
    regiones = OfertaEmpleo.objects.values('ubicacion').annotate(cantidad=Count('ubicacion')).order_by('-cantidad')
    return render(request, 'analisis_mercado/tendencias_regiones.html', {'regiones': regiones})

def tendencias_industrias(request):
    industrias = DatoMercado.objects.values('tendencias_industria').annotate(cantidad=Count('tendencias_industria')).order_by('-cantidad')
    return render(request, 'analisis_mercado/tendencias_industrias.html', {'industrias': industrias})
