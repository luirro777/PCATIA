from django import forms
from .models import Solicitud
from captcha.fields import CaptchaField

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
        labels = {
            'nombres_principal': 'Nombres',
            'apellidos_principal': 'Apellidos',
            'cargo_principal': 'Cargo',
            'institucion_principal': 'Institución',
            'ciudad_principal': 'Ciudad',
            'pais_principal': 'País',
            'rol_estudio_principal': 'Rol en el Estudio',
            'email_principal': 'Correo Electrónico',
            'telefono_principal': 'Teléfono',    
            'nombres_alterno': 'Nombres',
            'apellidos_alterno': 'Apellidos',
            'cargo_alterno': 'Cargo',
            'institucion_alterno': 'Institución',
            'ciudad_alterno': 'Ciudad',
            'pais_alterno': 'País',
            'rol_estudio_alterno': 'Rol en el Estudio',
            'email_alterno': 'Correo Electrónico',
            'telefono_alterno': 'Teléfono',    
            'uso_curricular': '¿Forma parte de un estudio curricular?',
            'carrera_posgrado': 'Carrera de Posgrado',
            'estudiantes': 'Estudiantes',
            'responsables_orientacion': 'Responsables de Orientación',            
            'titulo_estudio': 'Título del Estudio',
            'objetivo': 'Objetivo',
            'descripcion_metodologia': 'Descripción de la Metodología',
            'caracteristicas_poblacion': 'Características de la Población',
            'utilidad_estudio': 'Utilidad del Estudio',
            'institucion_avala': 'Institución que Avala',
        }
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(SolicitudForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True  # Marcar todos los campos como obligatorios
        # Quitar unos campos puntuales
        self.fields['carrera_posgrado'].required = False
        self.fields['estudiantes'].required = False
        self.fields['responsables_orientacion'].required = False


    def clean(self):
        # Llamada al clean de la superclase para obtener los datos validados previamente
        cleaned_data = super().clean()

        # Validación de "uso_curricular" y los campos relacionados
        uso_curricular = cleaned_data.get('uso_curricular')
        carrera_posgrado = cleaned_data.get('carrera_posgrado')
        estudiantes = cleaned_data.get('estudiantes')
        responsables_orientacion = cleaned_data.get('responsables_orientacion')

        if uso_curricular == 'Sí':
            if not carrera_posgrado:
                self.add_error('carrera_posgrado', 'Este campo es obligatorio si el uso curricular es "Sí".')
            if not estudiantes:
                self.add_error('estudiantes', 'Este campo es obligatorio si el uso curricular es "Sí".')
            if not responsables_orientacion:
                self.add_error('responsables_orientacion', 'Este campo es obligatorio si el uso curricular es "Sí".')

        # Validación de que la información del responsable principal no sea igual a la del responsable alterno
        nombres_principal = cleaned_data.get('nombres_principal')
        apellidos_principal = cleaned_data.get('apellidos_principal')
        email_principal = cleaned_data.get('email_principal')
        telefono_principal = cleaned_data.get('telefono_principal')

        nombres_alterno = cleaned_data.get('nombres_alterno')
        apellidos_alterno = cleaned_data.get('apellidos_alterno')
        email_alterno = cleaned_data.get('email_alterno')
        telefono_alterno = cleaned_data.get('telefono_alterno')

        # Comparación entre los datos de "principal" y "alterno"
        if (
            (nombres_principal == nombres_alterno and
            apellidos_principal == apellidos_alterno) or
            email_principal == email_alterno or
            telefono_principal == telefono_alterno
        ):
            raise forms.ValidationError("La información del responsable principal no puede ser igual a la del responsable alterno.")

        # Validacion del telefono        
        if not telefono_principal.isdigit():
            raise forms.ValidationError("El teléfono solo debe contener números.")
        if not telefono_alterno.isdigit():
            raise forms.ValidationError("El teléfono solo debe contener números.")
        
        # Retornamos los datos validados
        return cleaned_data