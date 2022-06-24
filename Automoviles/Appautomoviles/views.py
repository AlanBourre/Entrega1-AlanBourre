from django.shortcuts import render
from .models import *

def index(request):
    automovil = Automovil.objects.all()
    personal = Personal.objects.all()
    cliente = Cliente.objects.all()
    contexto = {"automovil": automovil, "personal": personal, "cliente": cliente} 
    return render(request, "Appautomoviles/index.html", contexto)
