import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from .base import *

ALLOWED_HOSTS = ['moroccan-solutions.com', 'www.moroccan-solutions.com']

# CSRF and Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Sentry
sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=0.5,
    send_default_pii=True,
)
