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
        fields = ("marca", "modelo", "tipo", "color","condicion","anio","kms", "precio")

class FormPersonal(ModelForm):
    class Meta():
        model = Personal
        fields = ("nombre", "apellido", "email", "telefono")

class UserRegisterForm(UserCreationForm):

    avatar = forms.ImageField(label="Avatar", required=False)
    username = forms.CharField(label="Nombre de usuario")
    email= forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ["avatar","username", "email", "password1", "password2", "first_name", "last_name"]

        # help_texts= {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    avatar = forms.ImageField(label="Avatar", required=False)
    username = forms.CharField(label="Nombre de usuario", required=False)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput, required= False)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput, required= False) 
    first_name = forms.CharField(label="Nombre", required= False)
    last_name = forms.CharField(label="Apellido", required= False)

    class Meta:
        model = User
        fields = ["avatar","username","email", "password1", "password2", "first_name", "last_name"]

        help_texts = {k: "" for k in fields}    

class FormAvatar(ModelForm):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']