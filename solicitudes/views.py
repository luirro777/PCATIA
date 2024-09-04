from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import (DetailView, DeleteView, ListView, TemplateView)
from django.views.generic.edit import FormView
from .models import Solicitud
from .forms import SolicitudForm

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