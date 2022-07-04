from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),

    path("personal/", views.personal, name="personal"),
    path("cliente/", views.cliente, name="cliente"),
    path("automovil/", views.automovil, name="automovil"),
    path("formulario_cliente/", views.formulario_cliente, name="formulario_cliente"),
    path("formulario_automovil/", views.formulario_automovil, name="formulario_automovil"),
    path("formulario_personal/", views.formulario_personal, name="formulario_personal"),
    path("buscar_automovil/", views.buscar_automovil, name="buscar_automovil"),
    path("eliminar_automovil/<auto_id>", views.eliminar_automovil, name="eliminar_automovil"),
    path("editar_automovil/<auto_id>", views.editar_automovil, name="editar_automovil"),    
    #path("base/", views.base),
]