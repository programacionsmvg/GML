from django.db import models

class Recomendacion(models.Model):
    usuario = models.ForeignKey('gestion_usuarios.Usuario', on_delete=models.CASCADE)
    tarea_sugerida = models.ForeignKey('gestion_proyectos_tareas.Tarea', on_delete=models.CASCADE)
    probabilidad_acierto = models.FloatField()

    def __str__(self):
        return f"Recomendación para {self.usuario.nombre}: {self.tarea_sugerida.nombre} ({self.probabilidad_acierto:.2f}%)"