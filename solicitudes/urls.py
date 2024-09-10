from django.urls import path
from .views import SolicitudCreateView, SolicitudEnviadaView, SolicitudListView, SolicitudDeleteView, SolicitudDetailView, GenerarDocumentoView, DescargarDocumentoView
from django.views.generic.base import TemplateView  # Importa TemplateView

app_name = 'solicitudes'

urlpatterns = [
    path('solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('solicitud-enviada/', SolicitudEnviadaView.as_view(), name='solicitud_enviada'),
    path('solicitudes/', SolicitudListView.as_view(), name='solicitud-list'),
    path('solicitudes/<int:pk>/', SolicitudDetailView.as_view(), name='solicitud_detail'),    
    path('solicitudes/<int:pk>/borrar/', SolicitudDeleteView.as_view(), name='solicitud_delete'),
    path('generar_documento/<int:pk>/', GenerarDocumentoView.as_view(), name='generar_documento'),
    path('descargar_documento/<str:file_name>/', DescargarDocumentoView.as_view(), name='descargar_documento'),    
]
