"""
Django settings for miettes project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import environ



env = environ.Env(

    DEBUG=(bool, False)
)



# Build paths nside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG_MODE") 

ALLOWED_HOSTS = [env("STATIC_IP"),env("PRODUCTION_IP"),env("PRODUCTION_IP_2")]
ADMINS = [('Hadi', env("ADMIN_EMAIL"))]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MA',
    'djmoney',
    'phonenumber_field',
    'livereload',
    'colorfield',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'miettes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'MA.views.cart_view',
                'MA.views.navbar_view'

            ],
        },
    },
]

WSGI_APPLICATION = 'miettes.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': env("ENGINE"),
        'NAME': env("NAME"),
        'USER': env("USER_DB"),
        'PASSWORD': env("PASSWORD"),
        'HOST': env("HOST"),
        'PORT': env("PORT"),
    },
    "example_db": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}






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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Beirut'

USE_I18N = True

USE_L10N = True

USE_TZ = True 


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
IMG_DIR = 'static/images'


# Media files
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = "/media/" 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#Email Settings

ENGINE = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_CONNECTIONS = {
    'noreply': {

        "host" : env("EMAIL_HOST"),
        "use_tls" : False,
        "use_ssl" : True,
        "port" : 465,
        "username" : env("EMAIL_HOST_USER_NOREPLY"),
        "password" : env("EMAIL_HOST_PASSWORD"),
},
    'support': {
        "host" : env("EMAIL_HOST"),
        "use_tls" : False,
        "use_ssl" : True,
        "port" : 465,
        "username" : env("EMAIL_HOST_USER_SUPPORT"),
        "password" : env("EMAIL_HOST_PASSWORD"),


    },
    'newsletter': {
        "host" : env("EMAIL_HOST"),
        "use_tls" : False,
        "use_ssl" : True,
        "port" : 465,
        "username" : env("EMAIL_HOST_USER_NEWSLETTER"),
        "password" : env("EMAIL_HOST_PASSWORD_NEWSLETTER"),


    }
}

EMAIL_CONNECTION_DEFAULT = 'noreply'


#DJANGO image fields

DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'WEBP'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'WEBP': ".webp","JPEG": ".jpg","PNG": ".png"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = False