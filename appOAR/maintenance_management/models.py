from django.db import models
from django.conf import settings
# Create your models here.

class TypeMaintenance(models.TextChoices):
    PREVENTIVO = 'PM', 'Preventivo'
    CORRECTIVO = 'CM', 'Correctivo'
    OVERHAUL = 'OV', 'Overhaul'

class Tools(models.Model):
    typeMaintenance = models.CharField(max_length=10, choices=TypeMaintenance.choices)
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    brand = models.CharField(max_length=200, blank=True)
    model = models.CharField(max_length=200, blank=True)
    usernumber = models.CharField(max_length=200, blank=True)
    receiptInspection = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return "Tools: %s name: %s "%(self.name,self.model)
    class Meta:
        verbose_name='tool'
        verbose_name_plural='tools'

class StateEnum(models.TextChoices):
    ABIERTA = 'AB', 'Abierta'
    CERRADA = 'CR', 'Cerrada'

class WorkOrder(models.Model):
    name = models.CharField(max_length=200, blank=True)
    consecutive = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=10, choices=StateEnum.choices)
    userApplicant = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    endDate=models.DateTimeField(auto_now_add=True)
    tools=models.ManyToManyField(Tools)
    place = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return "WORK ORDER: %s init Date: %s "%(self.name,self.created)
    class Meta:
        verbose_name='work_order'
        verbose_name_plural='work_orders'



    
    