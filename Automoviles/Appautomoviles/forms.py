from django.forms import ModelForm
from .models import *

class FormCliente(ModelForm):
    class Meta():
        model = Cliente
        fields = ("nombre", "apellido", "cuil", "direccion", "dni", "email")

class FormAutomovil(ModelForm):
    class Meta():
        model = Automovil
        fields = ("marca", "modelo", "tipo", "color", "precio")

class FormPersonal(ModelForm):
    class Meta():
        model = Personal
        fields = ("nombre", "apellido", "dni", "email")
