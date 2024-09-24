# production.py
from .base import *

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'cambiar-en-produccion')

ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
