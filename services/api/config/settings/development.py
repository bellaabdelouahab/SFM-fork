from .base import *

import os
import logging
from config.utils.postgres_checker import ensure_database_exists

logger = logging.getLogger(__name__)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-key-change-this')

# ALLOWED HOSTS
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Get database settings from environment
DB_NAME = os.environ.get('DB_NAME', 'moroccan_solutions_db')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
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
    }
}

# Email - Use console backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable security features that make development harder
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

# CORS - More permissive for development
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = get_env_list('CORS_ALLOWED_ORIGINS', 'http://localhost:3000,http://localhost:8000')

# Redis Cache - simple configuration for development
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', 'redis://localhost:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Allauth protocol setting for development
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # More relaxed for development

# Static files finders for development
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
