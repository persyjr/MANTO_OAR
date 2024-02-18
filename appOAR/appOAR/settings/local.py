from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


#PARA TRABAJAR CON db.sqlite#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
#para trabajar con postgreSql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'articulosclientes',
        'USER': 'postgres',
        'PASSWORD': 'sql_2023',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}
"""

STATIC_URL = 'static/'

#RUTA PARA MANEJO Y ARCHIVOS DE IMAGEN EN ADMIN
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

## Email de configuración.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend" # Para enviar correos con gmail
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587  ## Puerto para conectarse a GMAIL
EMAIL_HOST_USER="gerencia.greenriver@gmail.com"   ### Correo del remitente
EMAIL_HOST_PASSWORD="xdyo ddqt cxbw jrdf"    #### Contraseña del email del remitente