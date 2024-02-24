from django import forms
from . import models as m
#from servicios.forms import ImagePathWidget

class OrdenDeTrabajoForm(forms.ModelForm):
    class Meta:
        model = m.OrdenDeTrabajo
        fields = '__all__'
        #exclude = ["fecha_creacion"]
        """
        widgets={
            'adjunto_creacion':ImagePathWidget,
        }"""