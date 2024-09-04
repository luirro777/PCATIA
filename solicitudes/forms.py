from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        exclude = ['fecha_solicitud'] 
        widgets = {
            'objetivo': forms.Textarea(attrs={'rows': 3}),
            'descripcion_metodologia': forms.Textarea(attrs={'rows': 5}),
            'caracteristicas_poblacion': forms.Textarea(attrs={'rows': 3}),
            'utilidad_estudio': forms.Textarea(attrs={'rows': 3}),
        }
   