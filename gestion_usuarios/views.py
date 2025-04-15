# gestion_usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_proyectos')  # Redirige a la lista de proyectos
    else:
        form = UserCreationForm()
    return render(request, 'gestion_usuarios/registro.html', {'form': form})

# TODO: Implementar vistas para inicio de sesión y gestión de usuarios