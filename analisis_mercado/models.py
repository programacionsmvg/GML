# analisis_mercado/models.py
from django.db import models

class DatoMercado(models.Model):
    fecha = models.DateField()
    habilidades_demandadas = models.TextField()
    tendencias_region = models.TextField()
    tendencias_industria = models.TextField()

    def __str__(self):
        return f"Tendencias del {self.fecha}"