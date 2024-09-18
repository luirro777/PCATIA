from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('solicitudes/', include('solicitudes.urls')),
    path('accounts/', include('accounts.urls')),
    path('captcha/', include('captcha.urls')),
]
