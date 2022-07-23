from .base import *# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(m$23o+ry$aerd-p@f3er6@r++*zrv9y3da6l^v*)cgt2hl8*q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER':'root',
        'PASSWORD':'root',
        'NAME':'ecomercedb',
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
STATIC_URL = 'static/'
