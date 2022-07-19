from django.test import TestCase
from .models import *

# Create your tests here.

#Probamos crear un empleado.
class PersonalTest(TestCase):

    def setUp(self):
        Personal.objects.create(nombre="Juan", apellido="Perez",email="juanp@gmail.com", telefono= "1167840032")
        
    def test_personal_nombre(self):
        personal = Personal.objects.get(nombre="Juan")
        self.assertEqual(personal.apellido, "Perez")
    
    def test_personal_creado(self):
        personal = Personal.objects.get(nombre="Juan")
        self.assertNotEquals(personal, None)

#Probamos crear un cliente.
class ClienteTest(TestCase):

    def setUp(self):
        Cliente.objects.create(nombre="Paco", apellido="Picapiedra", cuil="20-35223876-8", direccion= "Av. del Libertador - 4785",dni= "35223876", email="ppica@gmail.com")
        
    def test_Cliente_nombre(self):
        cliente = Cliente.objects.get(nombre="Paco")
        self.assertEqual(cliente.apellido, "Picapiedra")
    
    def test_Cliente_creado(self):
        cliente = Cliente.objects.get(nombre="Paco")
        self.assertNotEquals(cliente, None)

#Probamos crear un automóvil.
class AutomovilTest(TestCase):

    def setUp(self):
        Automovil.objects.create(marca="Peugeot", modelo="208", tipo="3", color= "Amarillo",condicion= "1", anio="2022", kms="0", precio=5000000, imagen="https://www.diariomotor.com/imagenes/picscache/1920x1600c/peugeot-208-2019-amarillo-exterior-18_1920x1600c.jpg")
        
    def test_Automovil_marca(self):
        automovil = Automovil.objects.get(marca="Peugeot")
        self.assertEqual(automovil.modelo, "208")
    
    def test_Automovil_creado(self):
        automovil = Automovil.objects.get(marca="Peugeot")
        self.assertNotEquals(automovil, None)
        