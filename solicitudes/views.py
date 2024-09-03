from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .models import Solicitud
from .forms import SolicitudForm

class SolicitudCreateView(FormView):    
    form_class = SolicitudForm
    template_name = 'solicitudes/solicitud_form.html'
    success_url = reverse_lazy('solicitudes:solicitud_enviada')

    def form_valid(self, form):
        # Guardar la solicitud en la base de datos
        form.save()      
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Aquí puedes imprimir los errores para depuración
        print(form.errors.as_data())
        return super().form_invalid(form)

class SolicitudEnviadaView(TemplateView):
    template_name = 'solicitudes/solicitud_enviada.html'