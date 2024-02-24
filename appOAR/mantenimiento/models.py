from django.db import models
from django.conf import settings
# Create your models here.

class TipoDeMantenimiento(models.TextChoices):
    PREVENTIVO = 'PM', 'Preventivo'
    CORRECTIVO = 'CM', 'Correctivo'
    OVERHAUL = 'OV', 'Overhaul'
    GARANTIA = 'GR', 'Garantía'

class Herramienta(models.Model):
    tipo_mantenimiento = models.CharField(max_length=10, choices=TipoDeMantenimiento.choices)
    nombre = models.CharField(max_length=200,  blank=True, null=True)
    descripcion = models.CharField(max_length=200,  blank=True, null=True)
    fabricante = models.CharField(max_length=200,  blank=True, null=True)
    parte_numero = models.CharField(max_length=200, blank=True, null=True)
    serie_numero = models.CharField(max_length=200,  blank=True, null=True)
    inspeccion_de_recibo = models.CharField(max_length=200,  blank=True, null=True)
    
    def __str__(self):
        return "Herramienta: %s nombre: %s "%(self.nombre,self.parte_numero)
    class Meta:
        verbose_name='herramienta'
        verbose_name_plural='herramientas'

class EstadoEnum(models.TextChoices):
    ABIERTA = 'AB', 'Abierta'
    CERRADA = 'CR', 'Cerrada'

class OrdenDeTrabajo(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    consecutivo = models.CharField(max_length=200)
    estado = models.CharField(max_length=10, choices=EstadoEnum.choices)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_cierre=models.DateTimeField(blank=True, null=True)
    herramienta=models.ManyToManyField(Herramienta, blank=True, null=True)
    lugar = models.CharField(max_length=200,  blank=True, null=True)
    
    def __str__(self):
        return "ORDEN DE TRABAJO: %s init Date: %s "%(self.nombre,self.fecha_creacion)
    class Meta:
        verbose_name='orden de trabajo'
        verbose_name_plural='ordenes de trabajo'



    
    