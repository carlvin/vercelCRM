# config/settings/dev_neon.py

from .base import *  # This imports os and other base settings

# Development Specific Settings
DEBUG = True

# Security Settings
# # Security Settings for Development
# CSRF_TRUSTED_ORIGINS = [
#     'http://*.127.0.0.1',
#     'http://localhost',
#     'http://*.localhost',
# ]

# ALLOWED_HOSTS = [
#     'localhost',
#     '127.0.0.1',
# ]

# # File Storage
# MEDIA_ROOT = "/home/media"
# STATIC_ROOT = "/home/static"

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PGDATABASE'),
        'USER': os.getenv('PGUSER'),
        'PASSWORD': os.getenv('PGPASSWORD'),
        'HOST': os.getenv('PGHOST'),
        'PORT': os.getenv('PGPORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require',
            'connect_timeout': 30,
            'keepalives': 1,
            'keepalives_idle': 30,
            'keepalives_interval': 10,
            'keepalives_count': 5,
        },
    }
}

# Development Tools
if DEBUG:

    CSRF_TRUSTED_ORIGINS = [
        'http://*.127.0.0.1',
        'http://localhost',
        'http://*.localhost',
    ]
   
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
    ]
    
    def show_toolbar(request):
        """Determine whether to show the toolbar."""
        return True
    
    INSTALLED_APPS += ['debug_toolbar']
    
    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE
    
    # DEBUG_TOOLBAR_CONFIG = {
    #     'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    #     'INSERT_BEFORE': '</body>',
    #     'SHOW_TEMPLATE_CONTEXT': True,
    #     'ENABLE_STACKTRACES': True,
    #     'RESULTS_CACHE_SIZE': 3,
    #     'SHOW_COLLAPSED': True,
    # }
    
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    # Email Backend for Development
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Disable HTTPS redirect in development
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_BROWSER_XSS_FILTER = False
    SECURE_CONTENT_TYPE_NOSNIFF = False
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False

# Validate required settings
def validate_db_settings():
    required_settings = ['PGDATABASE', 'PGUSER', 'PGPASSWORD', 'PGHOST']
    missing_settings = [
        setting for setting in required_settings 
        if not os.getenv(setting)
    ]
    if missing_settings:
        raise ImproperlyConfigured(
            f"Missing required database settings: {', '.join(missing_settings)}"
        )

# Run validation
validate_db_settings()

# from .base import *
# DEBUG = True

# CSRF_TRUSTED_ORIGINS = ['https://*.carlhub.com','https://*.127.0.0.1']

# INTERNAL_IPS = ['127.0.0.1',]

# ALLOWED_HOSTS = ['.vercel.app','.now.sh','carlhub.com','www.carlhub.com','localhost','127.0.0.1']

# SECRET_KEY="django-insecure-h*wprd2xbt#!jq#rrkr_ww2h(md#=bm&a0ok4h!tp(081%+6)6"

# MEDIA_ROOT = "/home/media"
# STATIC_ROOT = "/home/static"

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('PGDATABASE'),
#         'USER': os.getenv('PGUSER'),
#         'PASSWORD': os.getenv('PGPASSWORD'),
#         'HOST': os.getenv('PGHOST'),
#         'PORT': os.getenv('PGPORT', '5432'),
#         'OPTIONS': {
#             'sslmode': 'require',
#             'connect_timeout': 30,
#             'keepalives': 1,
#             'keepalives_idle': 30,
#             'keepalives_interval': 10,
#             'keepalives_count': 5,
#         },
#     }
# }
