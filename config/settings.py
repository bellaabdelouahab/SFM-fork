import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = "django-insecure-3rp#05un@&z8#x!tuksg11216m1we5o0@4g13f2+73-p3s76ur"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"] if DEBUG else os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Application definition
INSTALLED_APPS = [
    # Django built-ins
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "djongo",  # MongoDB connector
    "rest_framework",
    "corsheaders",
    "drf_yasg",  # API documentation
    "django_celery_beat",
    # "django_celery_results",  # Removed as we're using Redis directly
    "allauth",
    "allauth.account",
    "modeltranslation",  # For translations
    "storages",  # For S3 or similar storage
    "django_prometheus",  # For monitoring
    # Local apps
    "apps.accounts",
    "apps.providers",
    "apps.solutions",
    "apps.ai_engine",
    "apps.payments",
    "apps.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",  # Required for django-allauth
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# MongoDB Configuration
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "moroccan_solutions_db",
        "CLIENT": {
            "host": os.environ.get("MONGODB_URI", "mongodb://localhost:27017"),
            "username": os.environ.get("MONGODB_USERNAME", ""),
            "password": os.environ.get("MONGODB_PASSWORD", ""),
            "authSource": os.environ.get("MONGODB_AUTH_SOURCE", "admin"),
        },
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
