from .base import *
import sentry_sdk
import logging
from sentry_sdk.integrations.django import DjangoIntegration
from config.utils.postgres_checker import ensure_database_exists

logger = logging.getLogger(__name__)

# Security settings
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')  # Should be set in environment variables

# Hosts
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'moroccan-solutions.com,www.moroccan-solutions.com').split(',')

# Get database settings from environment
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT', '5432')

# Create database if it doesn't exist
try:
    db_created = ensure_database_exists(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    if db_created:
        logger.info(f"Database {DB_NAME} is ready")
except Exception as e:
    logger.error(f"Error ensuring database exists: {str(e)}")

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'CONN_MAX_AGE': 600,  # 10 minutes connection persistence
    }
}

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# CSRF and Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CORS settings
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = get_env_list('CORS_ALLOWED_ORIGINS', '')

# Redis Cache - production configuration
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SOCKET_CONNECT_TIMEOUT': 5,  # seconds
            'SOCKET_TIMEOUT': 5,  # seconds
            'IGNORE_EXCEPTIONS': True,
        }
    }
}

# Allauth settings
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Sentry
sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=0.5,
    send_default_pii=True,
    environment='production',
)

# Force HTTPS on all URLs
SECURE_SSL_REDIRECT = True

# Static files optimization
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
