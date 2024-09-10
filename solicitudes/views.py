from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import (DetailView, DeleteView, ListView, TemplateView, View)
from django.views.generic.edit import FormView
from .models import Solicitud
from .forms import SolicitudForm
from docxtpl import DocxTemplate
import uuid
import os
from django.core.files.storage import default_storage
from django.utils import timezone
from django.shortcuts import redirect
from django.http import HttpResponse

class SolicitudCreateView(FormView):    
    form_class = SolicitudForm
    template_name = 'solicitudes/solicitud_form.html'
    success_url = reverse_lazy('solicitudes:solicitud_enviada')

    def form_valid(self, form):       
        form.save()      
        return super().form_valid(form)
    
    def form_invalid(self, form):        
        print(form.errors.as_data())
        return super().form_invalid(form)

class SolicitudEnviadaView(TemplateView):
    template_name = 'solicitudes/solicitud_enviada.html'

class SolicitudListView(LoginRequiredMixin, ListView):
    model = Solicitud
    template_name = 'solicitudes/solicitud_list.html'
    context_object_name = 'solicitudes'
    login_url = '/login/' 

class SolicitudDeleteView(LoginRequiredMixin, DeleteView):
    model = Solicitud
    template_name = 'solicitudes/solicitud_confirm_delete.html'
    success_url = reverse_lazy('solicitud_list')

class SolicitudDetailView(LoginRequiredMixin, DetailView):
    model = Solicitud
    template_name = 'solicitudes/solicitud_detail.html'

# Generacion de docx
class GenerarDocumentoView(DetailView):
    model = Solicitud
    template_name = 'solicitudes/generar_documento.html'  # Una plantilla opcional si quieres mostrar algo en pantalla

    def get(self, request, *args, **kwargs):
        solicitud = self.get_object()

        # Cargar la plantilla del archivo .docx
        template = DocxTemplate('templates/ActaUso.docx')

        # Definir el contexto con los datos del formulario
        contexto = {            
            'nombres_principal': solicitud.nombres_principal,
            'apellidos_principal': solicitud.apellidos_principal,
            'cargo_principal': solicitud.cargo_principal,
            'institucion_principal': solicitud.institucion_principal,
            'ciudad_principal': solicitud.ciudad_principal,
            'pais_principal': solicitud.pais_principal,
            'titulo_estudio': solicitud.titulo_estudio, 
            'caracteristicas_poblacion': solicitud.caracteristicas_poblacion,
            'dia_solicitud': solicitud.fecha_solicitud.day,
            'mes_solicitud': solicitud.fecha_solicitud.month,
            'anio_solicitud': solicitud.fecha_solicitud.year,          
        }

        # Rellenar la plantilla
        template.render(contexto)

        # Generar un nombre único para el archivo
        file_name = f'documento_{uuid.uuid4()}.docx'

        # Guardar el archivo temporalmente
        file_path = os.path.join('media', 'temp_docs', file_name)
        template.save(file_path)

        # Redirigir a la vista de descarga con el archivo generado
        return redirect('solicitudes:descargar_documento', file_name=file_name)

class DescargarDocumentoView(View):
    
    def get(self, request, file_name):
        file_path = os.path.join('media', 'temp_docs', file_name)

        # Comprobar si el archivo existe
        if default_storage.exists(file_path):
            # Crear una respuesta HTTP con el archivo
            with default_storage.open(file_path, 'rb') as docx_file:
                response = HttpResponse(docx_file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = f'attachment; filename={file_name}'
                return response
        else:
            return HttpResponse("El enlace ha expirado o el archivo ya no está disponible.", status=404)