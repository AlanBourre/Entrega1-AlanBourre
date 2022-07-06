from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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
        fields = ("nombre", "apellido", "email", "telefono")

class UserRegisterForm(UserCreationForm):

    email= forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        help_texts= {k: "" for k in fields}
        