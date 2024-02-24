from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . import models as m
from . import forms as f

# Create your views here.
class listarOrdenesDeTrabajoView(generic.ListView):
    model=m.OrdenDeTrabajo
    template_name='list_ot.html'

class AddOrdendeTrabajoCreateView(generic.CreateView):
    model=m.OrdenDeTrabajo
    template_name='components/form_ordentrabajo.html'
    form_class=f.OrdenDeTrabajoForm
    success_url = reverse_lazy('mantenimiento:ordenesdetrabajo')

class ActualizarTicketPUCView(generic.UpdateView):
    model=m.OrdenDeTrabajo
    template_name='components/form_ordentrabajo.html'
    form_class=f.OrdenDeTrabajoForm
    success_url = reverse_lazy('mantenimiento:ordenesdetrabajo')

class EliminarOrdenDeTrabajoView(generic.DeleteView):
    model=m.OrdenDeTrabajo
    template_name='components/form_deleteordentrabajo.html'
    success_url = reverse_lazy('mantenimiento:ordenesdetrabajo')