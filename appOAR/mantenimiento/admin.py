from django.contrib import admin
from mantenimiento import models as m
# Register your models here.

@admin.register(m.OrdenDeTrabajo)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_creacion','consecutivo')

@admin.register(m.Herramienta)
class Tools(admin.ModelAdmin):
    readonly_fields=('parte_numero','serie_numero')