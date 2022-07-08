from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil"),
    path("agregar_avatar", views.agregar_avatar, name="agregar_avatar"),
    path("about", views.about, name="about"),


    path("personal/", views.personal, name="personal"),
    path("cliente/", views.cliente, name="cliente"),
    path("automovil/", views.automovil, name="automovil"),
    path("formulario_cliente/", views.formulario_cliente, name="formulario_cliente"),
    path("formulario_automovil/", views.formulario_automovil, name="formulario_automovil"),
    path("formulario_personal/", views.formulario_personal, name="formulario_personal"),
    path("buscar_automovil/", views.buscar_automovil, name="buscar_automovil"),
    path("eliminar_automovil/<auto_id>", views.eliminar_automovil, name="eliminar_automovil"),
    path("editar_automovil/<auto_id>", views.editar_automovil, name="editar_automovil"),
    path("eliminar_cliente/<client_id>", views.eliminar_cliente, name="eliminar_cliente"),
    path("editar_cliente/<client_id>", views.editar_cliente, name="editar_cliente"),
    path("eliminar_personal/<persona_id>", views.eliminar_personal, name="eliminar_personal"),
    path("editar_personal/<persona_id>", views.editar_personal, name="editar_personal"),    
    #path("base/", views.base),
]