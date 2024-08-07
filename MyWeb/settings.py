"""
Django settings for MyWeb project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gu9=6bm9rqw8u&ulib05+!pf&w!d)o^)*i91=p0l@75lb5_6d)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
LOGIN_REDIRECT_URL ='/'
LOGOUT_REDIRECT_URL ='/'
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MyApp',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Esta línea debe incluir la ubicación de tus templates

        
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': str (BASE_DIR / 'db.sqlite3'),
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#AUTH_USER_MODEL = 'MyApp.auth.User'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


#es la ruta a tu backend de autenticación personalizado.
#AUTHENTICATION_BACKENDS = ['path.to.your.EmailBackend']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # El servidor SMTP que estás utilizando
EMAIL_PORT = 587  # Puerto SMTP
EMAIL_USE_TLS = True  # O False si no se requiere TLS
EMAIL_HOST_USER = 'kraquen8686@gmail.com'  # Nombre de usuario para el servidor SMTP
EMAIL_HOST_PASSWORD = 'szbm kowr gmao himv'  # Contraseña para el servidor SMTP



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configuración de archivos de medios
MEDIA_URL = '/image/'
# Define una sola vez MEDIA_ROOT
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Define las subcarpetas para cada banda dentro de MEDIA_ROOT
INDIO_SOLARI_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'Indio_Solari')
LA_RENGA_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'La_Renga')
DIVIDIDOS_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'Divididos')
LAS_PELOTAS_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'Las_Pelotas')
CIRO_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'Ciro')
NTVG_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'ntvg')



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py

# Configuración de la sesión
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # La sesión expira al cerrar el navegador

SESSION_COOKIE_AGE = 2800  # 30 minutos en segundos. Esto mantendrá la sesión activa durante 30 minutos de inactividad.


