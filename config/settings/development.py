from .base import *

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-key-change-this')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get('MONGODB_NAME', 'moroccan_solutions_db'),
        'CLIENT': {
            'host': os.environ.get('MONGODB_URI', 'mongodb://localhost:27017'),
            'username': os.environ.get('MONGODB_USERNAME', ''),
            'password': os.environ.get('MONGODB_PASSWORD', ''),
            'authSource': os.environ.get('MONGODB_AUTH_SOURCE', 'admin'),
        }
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Add this to ensure static files are properly served in development
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
