from django.shortcuts import render
from .models import *

def index(request):
    automovil = Automovil.objects.all()
    personal = Personal.objects.all()
    cliente = Cliente.objects.all()
    contexto = {"automovil": automovil, "personal": personal, "cliente": cliente} 
    return render(request, "Appautomoviles/index.html", contexto)

def personal(request):
    personal = Personal.objects.all()
    return render(request, "Appautomoviles/personal.html", {"personal": personal})

def cliente(request):
    cliente = Cliente.objects.all()
    return render(request, "Appautomoviles/cliente.html", {"cliente": cliente})

def automovil(request):
    automovil = Automovil.objects.all()
    return render(request, "Appautomoviles/automovil.html", {"automovil": automovil})

def formulario_cliente(request):

    if request.method == "GET":
        return render(request, "Appautomoviles/formulario_cliente.html", {})

    elif request.method == "POST":

        info_formulario = request.POST
        cliente = Cliente(info_formulario["nombre"], info_formulario["apellido"])

        cliente.save()

        return render(request, "Appautomoviles/formulario_cliente.html", {})

    else:
        return render(request, "Appautomoviles/formulario_cliente.html", {})

    return render(request, "Appautomoviles/formulario_cliente.html", {})


def base(request):

    return render(request, "Appautomoviles/base.html", {})
