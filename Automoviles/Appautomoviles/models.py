from django.db import models

class Automovil(models.Model):
    marca = models.CharField("Marca", max_length=20)
    modelo = models.CharField("Modelo", max_length=30)
    TIPOS = (
        (1, "Sedan"),
        (2, "Suv"),
        (3, "Hatchback"),
        (4, "Deportivos"),
        (5, "Van"),
        (6, "Pick up")
    )
    tipo = models.PositiveSmallIntegerField("Tipo", choices=TIPOS)
    color = models.CharField("Color", max_length=15)
    precio = models.FloatField("Precio $")

    class Meta:
        verbose_name_plural = "Automoviles"
    

class Personal(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    dni = models.CharField("DNI", max_length=8)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Personal"


class Cliente(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    cuil = models.CharField("CUIL", max_length=13)
    direccion = models.CharField("Direccion", max_length=50)
    dni = models.CharField("DNI", max_length=8)
    email = models.EmailField(blank=True, null=True)

    #hola
