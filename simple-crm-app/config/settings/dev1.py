from .base import *
DEBUG = True

CSRF_TRUSTED_ORIGINS = ['https://*.carlhub.com','https://*.127.0.0.1']

INTERNAL_IPS = ['127.0.0.1',]

ALLOWED_HOSTS = ['carlhub.com','www.carlhub.com','localhost','127.0.0.1']

SECRET_KEY="django-insecure-h*wprd2xbt#!jq#rrkr_ww2h(md#=bm&a0ok4h!tp(081%+6)6"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carlhub',
        'USER':'carlhub',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT':"",
    }
}
