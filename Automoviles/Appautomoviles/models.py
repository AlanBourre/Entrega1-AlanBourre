from django.db import models
from django.contrib.auth.models import *

class Automovil(models.Model):
    marca = models.CharField("Marca", max_length=20)
    modelo = models.CharField("Modelo", max_length=30)
    TIPOS = (
        (1, "Sedan"),
        (2, "Suv"),
        (3, "Hatchback"),
        (4, "Deportivo"),
        (5, "Van"),
        (6, "Pick up")
    )
    tipo = models.PositiveSmallIntegerField("Tipo", choices=TIPOS)
    color = models.CharField("Color", max_length=15)
    CONDICION = (
        (1, "Nuevo"),
        (2, "Usado"),
    )
    condicion = models.PositiveSmallIntegerField("Condición", choices=CONDICION)
    anio = models.CharField("Año", max_length=4)
    kms = models.FloatField("Kilometros")
    precio = models.FloatField("Precio $")
    imagen = models.ImageField(upload_to="imagenes/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Automoviles"
    

class Personal(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField("Teléfono", max_length=15) #AGREGADO

    class Meta:
        verbose_name_plural = "Personal"


class Cliente(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    cuil = models.CharField("CUIL", max_length=13)
    direccion = models.CharField("Dirección", max_length=50)
    dni = models.CharField("DNI", max_length=8)
    email = models.EmailField(blank=True, null=True)


class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatar/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Avatares"

class Comentario(models.Model):
  autor = models.ForeignKey(User,on_delete=models.CASCADE)
  automovil = models.ForeignKey(Automovil, related_name="comments" ,on_delete=models.CASCADE)
  comentario = models.TextField()
  fecha = models.DateTimeField(auto_now_add=True)