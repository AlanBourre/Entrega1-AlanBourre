from django.forms import ModelForm
from .models import *

class FormCliente(ModelForm):
    class Meta():
        model = Cliente
        fields = ("nombre", "apellido", "cuil", "direccion", "dni", "email")
