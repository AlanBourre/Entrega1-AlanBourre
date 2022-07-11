from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def entrada(request):
    return redirect("index")

def index(request):
    automovil = Automovil.objects.all()
    personal = Personal.objects.all()
    cliente = Cliente.objects.all()
    contexto = {"automovil": automovil, "personal": personal, "cliente": cliente}

    # if request.user.is_authenticated:
    #     avatar= Avatar.objects.get(usuario= request.user)
    #     return render(request, "Appautomoviles/index.html", contexto,{"avatar": avatar})

    return render(request, "Appautomoviles/index.html", contexto)

def about(request):
    
    return render(request, 'Appautomoviles/about.html')

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("login")
        else:
            return redirect("login")

    form= AuthenticationForm()

    return render(request, "Appautomoviles/login.html", {"form": form})

def logout_request(request):
    
    logout(request)
    return redirect("index")

@login_required
def editar_perfil(request):

    user = request.user

    if request.method == "POST":
        
        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]

            user.save()
            

            return redirect("index")

    else:
        form = UserEditForm(initial = {"email":user.email, "first_name": user.first_name, "last_name": user.last_name})

    return render(request, "Appautomoviles/editar_perfil.html", {"form": form}) 



@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
            
        form = FormAvatar(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            # avatar.save()

            return redirect("index")

    else:
        form = FormAvatar()
    
    return render(request, "Appautomoviles/agregar_avatar.html", {"form": form})

def register_request(request):

    if request.method == "POST":

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("login")            

        return render(request, "Appautomoviles/register.html", {"form": form})

    # form= UserCreationForm()
    form= UserRegisterForm() #este sirve para editarlo a nuestra manera

    return render(request, "Appautomoviles/register.html", {"form": form})

def personal(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            personal = Personal.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()

            return render(request,"Appautomoviles/personal.html",{"personal":personal, "search":True, "busqueda":search})

    personal = Personal.objects.all()

    return render(request,"Appautomoviles/personal.html",{"personal":personal})

@staff_member_required
def cliente(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            cliente = Cliente.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()

            return render(request,"Appautomoviles/cliente.html",{"cliente":cliente, "search":True, "busqueda":search})

    cliente = Cliente.objects.all()

    return render(request,"Appautomoviles/cliente.html",{"cliente":cliente})

def automovil(request):
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            automovil = Automovil.objects.filter( Q(marca__icontains=search) | Q(anio__icontains=search) | Q(tipo__icontains=search) ).values()  #(marca__icontains=search).values()

            return render(request,"Appautomoviles/automovil.html",{"automovil":automovil, "search":True, "busqueda":search})

    automovil = Automovil.objects.all()

    return render(request,"Appautomoviles/automovil.html",{"automovil":automovil})

@staff_member_required
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

@staff_member_required
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

@staff_member_required
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

@staff_member_required
def eliminar_automovil(request, auto_id):

    automovil = Automovil.objects.get(id=auto_id)
    automovil.delete()

    return redirect("automovil")

@staff_member_required
def eliminar_cliente(request, client_id):

    cliente = Cliente.objects.get(id=client_id)
    cliente.delete()

    return redirect("cliente")
    
@staff_member_required
def eliminar_personal(request, persona_id):

    personal = Personal.objects.get(id=persona_id)
    personal.delete()

    return redirect("personal")

@staff_member_required
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
            automovil.condicion = info_automovil["condicion"]
            automovil.anio = info_automovil["anio"]
            automovil.kms = info_automovil["kms"]
            automovil.precio = info_automovil["precio"]
            automovil.save()

            return redirect("automovil")

    #get
    formulario = FormAutomovil(initial= {"marca": automovil.marca, "modelo": automovil.modelo, "tipo": automovil.tipo,"color": automovil.color,"condicion": automovil.condicion,"anio": automovil.anio, "kms": automovil.kms, "precio": automovil.precio})
    contexto = {"form": formulario}

    return render(request, "Appautomoviles/formulario_automovil.html", contexto)

@staff_member_required
def editar_cliente(request, client_id):

    cliente = Cliente.objects.get(id=client_id)
    
    if request.method == "POST":
        
        formulario = FormCliente(request.POST)

        if formulario.is_valid():

            info_cliente = formulario.cleaned_data

            cliente.nombre = info_cliente["nombre"]
            cliente.apellido = info_cliente["apellido"]
            cliente.cuil = info_cliente["cuil"]
            cliente.direccion = info_cliente["direccion"]
            cliente.dni = info_cliente["dni"]
            cliente.email = info_cliente["email"]
            cliente.save()

            return redirect("cliente")

    #get
    formulario = FormCliente(initial= {"nombre": cliente.nombre, "apellido": cliente.apellido, "cuil": cliente.cuil,"direccion": cliente.direccion, "dni": cliente.dni, "email": cliente.email})
    contexto = {"form": formulario}

    return render(request, "Appautomoviles/formulario_cliente.html", contexto)

@staff_member_required
def editar_personal(request, persona_id):

    personal = Personal.objects.get(id=persona_id)
    
    if request.method == "POST":
        
        formulario = FormPersonal(request.POST)

        if formulario.is_valid():

            info_personal = formulario.cleaned_data

            personal.nombre = info_personal["nombre"]
            personal.apellido = info_personal["apellido"]            
            personal.email = info_personal["email"]
            personal.telefono = info_personal["telefono"]
            personal.save()

            return redirect("personal")

    #get
    formulario = FormPersonal(initial= {"nombre": personal.nombre, "apellido": personal.apellido, "email": personal.email, "telefono": personal.telefono})
    contexto = {"form": formulario}

    return render(request, "Appautomoviles/formulario_personal.html", contexto)

def buscar_automovil(request):

    if request.method == "POST":

        marca = request.POST["marca"]

        automoviles = Automovil.objects.filter(marca__icontains=marca).values()

        return render(request, "Appautomoviles/buscar_automovil.html", {"automoviles": automoviles})

    
    else:
        automoviles = []  #Automovil.objects.all()

        return render(request, "Appautomoviles/buscar_automovil.html", {"automoviles": automoviles})

def base(request):

    return render(request, "Appautomoviles/base.html", {})

def novedades(request):
    return render(request, 'Appautomoviles/novedades.html')
