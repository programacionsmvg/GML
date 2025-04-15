# inteligencia_artificial/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('recomendaciones/', views.recomendaciones, name='recomendaciones'),
    path('predicciones/', views.predicciones, name='predicciones'),
]