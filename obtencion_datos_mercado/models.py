# obtencion_datos_mercado/models.py
from django.db import models
from analisis_mercado.models import DatoMercado

class Habilidad(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class OfertaEmpleo(models.Model):
    titulo = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    salario = models.FloatField(null=True, blank=True)
    fecha_publicacion = models.DateField()
    datomercado = models.ForeignKey(DatoMercado, on_delete=models.SET_NULL, null=True, blank=True)
    habilidades = models.ManyToManyField(Habilidad, through='OfertaHabilidad')

    def __str__(self):
        return f"{self.titulo} en {self.empresa}"

class OfertaHabilidad(models.Model):
    oferta = models.ForeignKey(OfertaEmpleo, on_delete=models.CASCADE)
    habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('oferta', 'habilidad')