from django.contrib import admin

from . models import *

class AutomovilAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "tipo", "color","condicion","anio", "kms", "precio", "imagen")
    search_fields = ("marca", "modelo", "tipo", "color","condicion","anio", "kms", "precio", "imagen")

class PersonalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "telefono")
    search_fields = ("nombre", "apellido", "email", "telefono")

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "cuil", "direccion", "dni", "email")
    search_fields = ("nombre", "apellido", "cuil", "direccion","dni","email")

class AvatarAdmin(admin.ModelAdmin):
    list_display = ("usuario", "imagen")

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor','automovil','comentario','fecha')
    search_fields = ('autor','automovil','comentario','fecha')



admin.site.register(Automovil, AutomovilAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Comentario,ComentarioAdmin)