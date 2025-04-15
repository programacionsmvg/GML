from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('gestion_usuarios.urls')),
    path('proyectos/', include('gestion_proyectos_tareas.urls')),
    path('mercado/', include('obtencion_datos_mercado.urls')),
    path('analisis/', include('analisis_mercado.urls')),
    path('ia/', include('inteligencia_artificial.urls')),
]