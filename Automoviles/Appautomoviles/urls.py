from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("personal/", views.personal, name="personal"),
    path("cliente/", views.cliente, name="cliente"),
    path("automovil/", views.automovil, name="automovil"),
    path("formulario/", views.formulario, name="formulario"),
    #path("base/", views.base),
]