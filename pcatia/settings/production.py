from .base import *
import json
import os

DEBUG = True

# Ruta al archivo JSON
config_path = os.path.join(os.path.dirname(__file__), 'config.json')

# Cargar la configuración desde el archivo JSON
with open(config_path) as config_file:
    config = json.load(config_file)


ALLOWED_HOSTS = ['pcatia.luisromano.com.ar','localhost']

# Asignar las variables de configuración desde el JSON
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config['DJANGO_DB_NAME'],
        'USER': config['DJANGO_DB_USER'],
        'PASSWORD': config['DJANGO_DB_PASSWORD'],
        'HOST': config['DJANGO_DB_HOST'],
        'PORT': config['DJANGO_DB_PORT'],
    }
}

SECRET_KEY = config['DJANGO_SECRET_KEY']
os.environ['DJANGO_SETTINGS_MODULE'] = config['DJANGO_SETTINGS_MODULE']


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django_debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

