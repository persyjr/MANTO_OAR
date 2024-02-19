from django.contrib import admin
from maintenance_management import models as m
# Register your models here.

@admin.register(m.WorkOrder)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','consecutive')

@admin.register(m.Tools)
class Tools(admin.ModelAdmin):
    readonly_fields=('model','usernumber')