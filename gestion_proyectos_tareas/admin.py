from django.contrib import admin
from .models import Proyecto, Tarea, TareaUsuario

admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(TareaUsuario)