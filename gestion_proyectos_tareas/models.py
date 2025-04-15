# gestion_proyectos_tareas/models.py
from django.db import models
from gestion_usuarios.models import Usuario

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    gestor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos')

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=50, choices=[
        ('Pendiente', 'Pendiente'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada')
    ])
    prioridad = models.CharField(max_length=50, choices=[
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja')
    ])
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    asignados = models.ManyToManyField(Usuario, through='TareaUsuario', related_name='tareas_asignadas')

    def __str__(self):
        return f"{self.nombre} ({self.estado})"

class TareaUsuario(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tarea', 'usuario')

    def __str__(self):
        return f"{self.usuario.nombre} - {self.tarea.nombre}"