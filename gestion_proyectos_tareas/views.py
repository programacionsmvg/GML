# gestion_proyectos_tareas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto
from .forms import ProyectoForm

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'gestion_proyectos_tareas/lista_proyectos.html', {'proyectos': proyectos})

def crear_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'gestion_proyectos_tareas/formulario_proyecto.html', {'form': form})

def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'gestion_proyectos_tareas/formulario_proyecto.html', {'form': form})

def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    proyecto.delete()
    return redirect('lista_proyectos')