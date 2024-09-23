from django.contrib.auth.views import (
    LoginView,
    LogoutView,    
)
from .forms import CustomAuthenticationForm
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm 
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('solicitudes:solicitud_list')

class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

