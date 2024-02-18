from django.db import models
from django.conf import settings
# Create your models here.

class OrdenDeTrabajo(models.Model):
    solicitante=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE)# Preguntar si dejar configurado on_Delete para eliminar todo el historial 
    fecha_Creacion=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "OrdenDeTrabajo: %s creacion: %s "%(self.tipo,self.fecha_Creacion)
    class Meta:
        verbose_name='orden_de_trabajo'
        verbose_name_plural='ordenes_de_trabajo'
