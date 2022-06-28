from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

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

    if request.method == "POST":  #POST

        formulario = FormCliente(request.POST)

        if formulario.is_valid():

            formulario.save()

            return HttpResponseRedirect(reverse("cliente"))


    else:
        formulario = FormCliente()
    contexto = {"form": formulario}
    return render(request, "Appautomoviles/formulario_cliente.html", contexto)

    # else:  #GET Y OTROS

    #     formularioVacio = NuevoCliente()

    #     return render(request, "Appautomoviles/formulario_cliente.html", {"formularioVacio": formularioVacio})


def base(request):

    return render(request, "Appautomoviles/base.html", {})
