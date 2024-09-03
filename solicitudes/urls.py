from django.urls import path
from .views import SolicitudCreateView, SolicitudEnviadaView
from django.views.generic.base import TemplateView  # Importa TemplateView

app_name = 'solicitudes'

urlpatterns = [
    path('solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('solicitud-enviada/', SolicitudEnviadaView.as_view(), name='solicitud_enviada'),
]
