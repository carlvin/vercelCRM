import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured
from .logging_config import setup_logging


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent   
print(f'BASE_DIR: {BASE_DIR}')

def get_env(var_name, default=None):
    """Get environment variable or return explicit exception."""
    try:
        return os.getenv(var_name, default)
    except KeyError:
        error_msg = f'Set the {var_name} environment variable'
        raise ImproperlyConfigured(error_msg)

# Core Settings
DEBUG = get_env('DEBUG', 'False').lower() == 'true'
SECRET_KEY = get_env('SECRET_KEY')
DJANGO_SETTINGS_MODULE = get_env('DJANGO_SETTINGS_MODULE')

LOGGING = setup_logging(BASE_DIR)


# Custom variable to read enviroment variables in development
# READ_DOT_ENV_FILE = env.bool("READ_DOT_ENV_FILE",default=False)
# myvariable=os.getenv('DJANGO_SETTINGS_MODULE')
# print(f'This is running Module: { myvariable }' )

# # Get the value of an environmental variable
# DEBUG = os.getenv('DEBUG')
# SECRET_KEY = os.getenv('SECRET_KEY')

# Check if the environmental variable exists and retrieve its value
# if SECRET_KEY:
#     print(f"The SECRET_KEY is: {SECRET_KEY}")
# else:
#     print("SECRET_KEY is not set.")



#ALLOWED_HOSTS = ['127.0.0.1', 'localhost',]


# Application definition

DJANGO__APPS = [
    # while in dev(working on appending this)
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',     
]

THIRD_PARTY_APPS = [
    
    'django_htmx',
    #'django_htmx_refresh',
    'crispy_forms',
    'crispy_tailwind',
    #'ckeditor',
]
LOCAL_APPS = [
    'client_relationship_manager.apps.ClientRelationshipManagerConfig',  # Full path to app config
    'agents',
    'inventory',
]

INSTALLED_APPS = DJANGO__APPS + THIRD_PARTY_APPS + LOCAL_APPS

# This setting is used by custom middleware HtmxResponseMiddleware
# HTMX_APPS = LOCAL_APPS
HTMX_APPS = [
    # 'client_relationship_manager.apps.ClientRelationshipManagerConfig',  # Full path to app config
    'crm',
    'agents',
    'inventory',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    # 'django_htmx_refresh.middleware.HtmxResponseMiddleware',
    # 'middleware.HtmxResponseMiddleware',
     'middlewares.customMiddleware.HtmxTemplateResponseMiddleware.HtmxResponseMiddleware',
]

# ROOT_URLCONF = 'config.urls'

# BASE_TEMPLATES_DIR = BASE_DIR / 'templates'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / '../templates',
        ],
        'APP_DIRS': True,
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


# Files and Storage
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static_root'
STATICFILES_DIRS = [BASE_DIR / '../static']
STATICFILES_VENDOR_DIR = BASE_DIR / '../static/vendors'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media_root'

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Email Configuration
EMAIL_CONFIG = {
    'backend': get_env('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend'),
    'host': get_env('EMAIL_HOST', 'smtp.zoho.com'),
    'user': get_env('EMAIL_HOST_USER'),
    'password': get_env('EMAIL_HOST_PASSWORD'),
    'port': int(get_env('EMAIL_PORT', '587')),
    'use_tls': get_env('EMAIL_USE_TLS', 'True').lower() == 'true',
    'default_from': get_env('DEFAULT_FROM_EMAIL'),
}

EMAIL_BACKEND = EMAIL_CONFIG['backend']
EMAIL_HOST = EMAIL_CONFIG['host']
EMAIL_HOST_USER = EMAIL_CONFIG['user']
EMAIL_HOST_PASSWORD = EMAIL_CONFIG['password']
EMAIL_PORT = EMAIL_CONFIG['port']
EMAIL_USE_TLS = EMAIL_CONFIG['use_tls']
DEFAULT_FROM_EMAIL = EMAIL_CONFIG['default_from']

# Authentication
AUTH_USER_MODEL = 'client_relationship_manager.User'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
LOGOUT_REDIRECT_URL = "/"

# Security Settings
if not DEBUG:
    SECURE_SETTINGS = {
        'SECURE_PROXY_SSL_HEADER': ('HTTP_X_FORWARDED_PROTO', 'https'),
        'SECURE_SSL_REDIRECT': True,
        'SESSION_COOKIE_SECURE': True,
        'CSRF_COOKIE_SECURE': True,
        'SECURE_BROWSER_XSS_FILTER': True,
        'SECURE_CONTENT_TYPE_NOSNIFF': True,
        'SECURE_HSTS_SECONDS': 31536000,
        'SECURE_HSTS_INCLUDE_SUBDOMAINS': True,
        'SECURE_HSTS_PRELOAD': True,
        'X_FRAME_OPTIONS': "DENY",
    }
    globals().update(SECURE_SETTINGS)

# Additional Configurations
WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Third-party configurations
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}

# #modified to the new config folder
# WSGI_APPLICATION = 'config.wsgi.application'

# #ckeditor configuration
# CKEDITOR_CONFIGS = {
#     'awesome_ckeditor': {
#         'toolbar': 'Basic',
#     },
#      'default': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             ['Bold', 'Italic', 'Underline'],
#             ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
#             ['Link', 'Unlink'],
#             ['RemoveFormat', 'Source']
#         ]
#     }
# }


# # Database
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

# # Password validation
# # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
# # Modified location based on config folder
# # source (s) for python manage.py to collect static files
# STATICFILES_DIRS = [
#     BASE_DIR / '../static',
# ]
# # STATICFILES_DIRS = BASE_DIR / '../static'


# STATICFILES_VENDOR_DIR = BASE_DIR / '../static/vendors'

# MEDIA_URL =BASE_DIR / '/media/'
# MEDIA_ROOT = BASE_DIR / 'media_root'

# #ouput for python manage.py collectstatic
# #local cdn
# STATIC_ROOT = BASE_DIR / 'static_root'


# AUTH_USER_MODEL = 'client_relationship_manager.User'
# LOGIN_REDIRECT_URL = '/'
# LOGIN_URL = '/login'
# LOGOUT_REDIRECT_URL = "/"

# # Default primary key field type
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
# CRISPY_TEMPLATE_PACK = "tailwind"

# #test for development purposes
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "smtp.zoho.com"
# EMAIL_HOST_USER = "info@carlhub.com"
# EMAIL_HOST_PASSWORD = "zp!8lCkv"
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = "info@carlhub.com"



# if not DEBUG:
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
#     SECURE_BROWSER_XSS_FILTER = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     SECURE_HSTS_SECONDS = 31536000  # 1 year
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_PRELOAD = True
#     X_FRAME_OPTIONS = "DENY"
    
#     SECRET_KEY = os.environ['SECRET_KEY']
    
#     # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#     # EMAIL_HOST = env('EMAIL_HOST')
#     # EMAIL_HOST_USER = env('EMAIL_HOST_USER')
#     # EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
#     # EMAIL_USE_TLS = env('EMAIL_USE_TLS')
#     # EMAIL_PORT = env('EMAIL_PORT')
#     # DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
