from django import forms

class NuevoCliente(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    cuil = forms.CharField(max_length=13)
    direccion = forms.CharField(max_length=50)
    dni = forms.IntegerField(min_value=0)
    email = forms.EmailField()