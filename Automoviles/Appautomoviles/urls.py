from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("personal/", views.personal, name="personal"),
    path("cliente/", views.cliente, name="cliente"),
    path("automovil/", views.automovil, name="automovil"),
    path("formulario_cliente/", views.formulario_cliente, name="formulario_cliente"),
    #path("base/", views.base),
]