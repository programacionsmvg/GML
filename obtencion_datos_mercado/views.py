# obtencion_datos_mercado/views.py
from django.shortcuts import render
from .models import OfertaEmpleo, Habilidad, OfertaHabilidad
import requests
from bs4 import BeautifulSoup
from django.utils import timezone

def lista_ofertas(request):
    ofertas = OfertaEmpleo.objects.all()
    return render(request, 'obtencion_datos_mercado/lista_ofertas.html', {'ofertas': ofertas})

def extraer_ofertas():
    url = "https://www.infojobs.net/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    ofertas_html = soup.find_all("div", class_="oferta")  # Ajusta el selector CSS

    for oferta_html in ofertas_html:
        titulo = oferta_html.find("h2").text
        empresa = oferta_html.find("span", class_="empresa").text
        ubicacion = oferta_html.find("span", class_="ubicacion").text
        fecha_publicacion = timezone.now().date()  # o extrae la fecha del html.

        oferta = OfertaEmpleo.objects.create(
            titulo=titulo,
            empresa=empresa,
            ubicacion=ubicacion,
            fecha_publicacion=fecha_publicacion
        )

        # Extrae habilidades y crea relaciones
        habilidades_texto = oferta_html.find_all("span", class_="habilidad")
        for habilidad_texto in habilidades_texto:
            habilidad_nombre = habilidad_texto.text.strip()
            habilidad, creada = Habilidad.objects.get_or_create(nombre=habilidad_nombre)
            OfertaHabilidad.objects.create(oferta=oferta, habilidad=habilidad)

    return "Scraping exitoso"

def extraer_ofertas_tecnoempleo():
    url = "https://www.tecnoempleo.com/"  # Reemplaza con la URL real
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # TODO: Analizar el HTML de Tecnoempleo y extraer los datos necesarios
    # Ejemplo básico:
    for oferta in soup.find_all('div', class_='oferta'):
        titulo = oferta.find('h2').text
        empresa = oferta.find('span', class_='empresa').text
        # ... extraer otros datos ...

        # Guardar en la base de datos
        oferta_empleo = OfertaEmpleo.objects.create(
            titulo=titulo,
            empresa=empresa,
            # ... otros campos ...
            fecha_publicacion=timezone.now().date()
        )

        # Crear o asociar habilidades
        habilidades_texto = oferta.find('div', class_='habilidades').text.split(',')
        for habilidad_texto in habilidades_texto:
            habilidad_texto = habilidad_texto.strip()
            habilidad, created = Habilidad.objects.get_or_create(nombre=habilidad_texto)
            OfertaHabilidad.objects.create(oferta=oferta_empleo, habilidad=habilidad)

    return "Scraping_exitoso Tecnoempleo"

def extraer_ofertas_infojobs():
    url = "https://www.infojobs.net/"  # Reemplaza con la URL real
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # TODO: Analizar el HTML de InfoJobs y extraer los datos necesarios
    # Ejemplo básico:
    for oferta in soup.find_all('div', class_='oferta'):
        titulo = oferta.find('h2').text
        empresa = oferta.find('span', class_='empresa').text
        # ... extraer otros datos ...

        # Guardar en la base de datos
        oferta_empleo = OfertaEmpleo.objects.create(
            titulo=titulo,
            empresa=empresa,
            # ... otros campos ...
            fecha_publicacion=timezone.now().date()
        )

        # Crear o asociar habilidades
        habilidades_texto = oferta.find('div', class_='habilidades').text.split(',')
        for habilidad_texto in habilidades_texto:
            habilidad_texto = habilidad_texto.strip()
            habilidad, created = Habilidad.objects.get_or_create(nombre=habilidad_texto)
            OfertaHabilidad.objects.create(oferta=oferta_empleo, habilidad=habilidad)

    return "Scraping exitoso de Infojobs"

def extraer_ofertas_linkedin():
    url = "https://es.linkedin.com/"  # Reemplaza con la URL real
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # TODO: Analizar el HTML de LinkedIn y extraer los datos necesarios
    # Ejemplo básico:
    for oferta in soup.find_all('div', class_='oferta'):
        titulo = oferta.find('h2').text
        empresa = oferta.find('span', class_='empresa').text
        # ... extraer otros datos ...

        # Guardar en la base de datos
        oferta_empleo = OfertaEmpleo.objects.create(
            titulo=titulo,
            empresa=empresa,
            # ... otros campos ...
            fecha_publicacion=timezone.now().date()
        )

        # Crear o asociar habilidades
        habilidades_texto = oferta.find('div', class_='habilidades').text.split(',')
        for habilidad_texto in habilidades_texto:
            habilidad_texto = habilidad_texto.strip()
            habilidad, created = Habilidad.objects.get_or_create(nombre=habilidad_texto)
            OfertaHabilidad.objects.create(oferta=oferta_empleo, habilidad=habilidad)

    return "Scraping exitoso de Linkedin"