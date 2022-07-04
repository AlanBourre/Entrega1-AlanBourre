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
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            automovil = Automovil.objects.filter(marca__icontains=search).values()

            return render(request,"Appautomoviles/automovil.html",{"automovil":automovil, "search":True, "busqueda":search})

    automovil = Automovil.objects.all()

    return render(request,"Appautomoviles/automovil.html",{"automovil":automovil})

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

def formulario_automovil(request):

    if request.method == "POST":  #POST

        formulario = FormAutomovil(request.POST)

        if formulario.is_valid():

            formulario.save()

            return HttpResponseRedirect(reverse("automovil"))


    else:
        formulario = FormAutomovil()
    contexto = {"form": formulario}
    return render(request, "Appautomoviles/formulario_automovil.html", contexto)

def formulario_personal(request):

    if request.method == "POST":  #POST

        formulario = FormPersonal(request.POST)

        if formulario.is_valid():

            formulario.save()

            return HttpResponseRedirect(reverse("personal"))


    else:
        formulario = FormPersonal()
    contexto = {"form": formulario}
    return render(request, "Appautomoviles/formulario_personal.html", contexto)

def eliminar_automovil(request, auto_id):

    automovil = Automovil.objects.get(id=auto_id)
    automovil.delete()

    return redirect("automovil")

def editar_automovil(request, auto_id):

    automovil = Automovil.objects.get(id=auto_id)
    
    if request.method == "POST":
        
        formulario = FormAutomovil(request.POST)

        if formulario.is_valid():

            info_automovil = formulario.cleaned_data

            automovil.marca = info_automovil["marca"]
            automovil.modelo = info_automovil["modelo"]
            automovil.tipo = info_automovil["tipo"]
            automovil.color = info_automovil["color"]
            automovil.precio = info_automovil["precio"]
            automovil.save()

            return redirect("automovil")

    #get
    formulario = FormAutomovil(initial= {"marca": automovil.marca, "modelo": automovil.modelo, "tipo": automovil.tipo,"color": automovil.color, "precio": automovil.precio})
    contexto = {"form": formulario}

    return render(request, "Appautomoviles/formulario_automovil.html", contexto)

def buscar_automovil(request):

    if request.method == "POST":

        marca = request.POST["marca"]

        automoviles = Automovil.objects.filter(marca__icontains=marca) 

        return render(request, "Appautomoviles/buscar_automovil.html", {"automoviles": automoviles})

    
    else:
        automoviles = []  #Automovil.objects.all()

        return render(request, "Appautomoviles/buscar_automovil.html", {"automoviles": automoviles})


def base(request):

    return render(request, "Appautomoviles/base.html", {})
