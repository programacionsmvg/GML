from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    rol = models.CharField(max_length=50, choices=[
        ('Administrador', 'Administrador'),
        ('Gestor de Proyectos', 'Gestor de Proyectos'),
        ('Colaborador', 'Colaborador')
    ])
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="gestion_usuarios_groups",  # Añadir related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="gestion_usuarios_permissions",  # Añadir related_name
        related_query_name="user",
    )

    def __str__(self):
        return self.username