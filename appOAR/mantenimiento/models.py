from django.db import models
from django.conf import settings
# Create your models here.

class TipoDeMantenimiento(models.TextChoices):
    PREVENTIVO = 'PM', 'Preventivo'
    GARANTIA = 'GR', 'Garantía'
    CORRECTIVO = 'CM', 'Correctivo'
    OVERHAUL = 'OV', 'Overhaul'

class Herramienta(models.Model):
    tipo_mantenimiento = models.CharField(max_length=10, choices=TipoDeMantenimiento.choices)
    nombre = models.CharField(max_length=200, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)
    fabricante = models.CharField(max_length=200, blank=True)
    parte_numero = models.CharField(max_length=200, blank=True)
    serie_numero = models.CharField(max_length=200, blank=True)
    inspeccion_de_recibo = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return "Herramienta: %s nombre: %s "%(self.name,self.model)
    class Meta:
        verbose_name='herramienta'
        verbose_name_plural='herramientas'

class EstadoEnum(models.TextChoices):
    ABIERTA = 'AB', 'Abierta'
    CERRADA = 'CR', 'Cerrada'

class OrdenDeTrabajo(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    consecutivo = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=10, choices=EstadoEnum.choices)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_cierre=models.DateTimeField(auto_now_add=True)
    herramienta=models.ManyToManyField(Herramienta)
    lugar = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return "ORDEN DE TRABAJO: %s init Date: %s "%(self.name,self.created)
    class Meta:
        verbose_name='orden de trabajo'
        verbose_name_plural='ordenes de trabajo'



    
    