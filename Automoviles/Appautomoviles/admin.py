from django.contrib import admin

from . models import *

class AutomovilAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "tipo", "color", "precio")
    search_fields = ("marca", "precio")

class PersonalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "telefono")

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "cuil", "direccion", "dni", "email")



admin.site.register(Automovil, AutomovilAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Avatar)