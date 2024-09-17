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
            'email_principal': forms.EmailInput(),
            'email_alterno': forms.EmailInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super(SolicitudForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True  # Marcar todos los campos como obligatorios

    def clean_telefono_principal(self):
        telefono = self.cleaned_data.get('telefono_principal')
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono solo debe contener números.")        
        return telefono

    def clean(self):
        cleaned_data = super().clean()
        nombres_principal = cleaned_data.get('nombres_principal')
        apellidos_principal = cleaned_data.get('apellidos_principal')

        # Validar que el nombre y el apellido no sean iguales
        if nombres_principal == apellidos_principal:
            self.add_error('nombres_principal', 'El nombre y apellido no pueden ser iguales.')
        
        return cleaned_data