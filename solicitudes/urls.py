from django.urls import path
from .views import SolicitudCreateView, SolicitudEnviadaView, SolicitudListView, SolicitudDeleteView, SolicitudDetailView
from django.views.generic.base import TemplateView  # Importa TemplateView

app_name = 'solicitudes'

urlpatterns = [
    path('solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('solicitud-enviada/', SolicitudEnviadaView.as_view(), name='solicitud_enviada'),
    path('solicitudes/', SolicitudListView.as_view(), name='solicitud-list'),
    path('solicitudes/<int:pk>/', SolicitudDetailView.as_view(), name='solicitud_detail'),    
    path('solicitudes/<int:pk>/borrar/', SolicitudDeleteView.as_view(), name='solicitud_delete'),    
]
