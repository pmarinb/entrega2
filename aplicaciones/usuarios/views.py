from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Usuario
from .forms import Login
# Create your views here.


def vista_login(request):
    next = request.GET.get('next')
    form = Login(request.POST or None)
    if form.is_valid():
        nombre_usuario = form.cleaned_data.get('nombre_usuario')
        contrasenia = form.cleaned_data.get('contrasenia')
        usuario = authenticate(username=nombre_usuario, password=contrasenia)
        login(request, usuario)
        if next:
            return redirect(next)
        return redirect('/home')
    return render(request, "login.html", {'form': form})
