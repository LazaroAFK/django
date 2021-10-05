from django.http import FileResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# from django.template import context

@login_required(login_url='/login/')
def home(request):
    contexto = {
        "usuario": request.user.username,
        "nombre": request.user.get_full_name(),
        "nombre_corto": request.user.get_short_name(),
        "iniciales": request.user.first_name[0] + request.user.last_name[0],
        "correo": request.user.email,
        "grupo": request.user.groups.all()[0].name
    }
    return render(request, 'dashboard/home.html', contexto)

def login(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        if User.objects.filter(username = usuario).exists():
            context = {"existe_usuario" : True, "usuario" : usuario}
        else:
            context = {"existe_usuario" : False, "error" : "El usuario %s no existe." % usuario}

    else:
        context = {"existe_usuario" : False}
    return render(request, 'dashboard/login.html', context)

def password(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        contrasena = request.POST['contrasena']
        acceso = authenticate(request, username = usuario, password = contrasena)
        if acceso is not None:
            auth_login(request, acceso)
            return redirect('home')
        else:
            context = {"existe_usuario" : True, "usuario" : usuario, "error" : "La contraseña ingresada es incorrecta."}
            return render(request, 'dashboard/login.html', context)
    else:
        return redirect('home')

def logout(request):
    auth_logout(request)
    return redirect('login')