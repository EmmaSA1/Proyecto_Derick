from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from .message import message as Message


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión después del registro
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('home')  # Redirigir a la página principal
        else:
            # Agrega los errores de validación como mensajes de Django
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    message = Message(
        "info", 
        "Se a cerrado session exitosamente", 200, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8MIbugIhZBykSmQcR0QPcfnPUBOZQ6bm35w&s")
    return render(request, "login.html", {
        "message":json.dumps(message.to_dict())
        }
    )

@login_required
def home_view(request):
    return render(request, 'home.html')
