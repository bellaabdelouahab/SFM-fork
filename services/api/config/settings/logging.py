import os


# Logging Configuration
import structlog
import logging
from pythonjsonlogger import jsonlogger
from colorlog import ColoredFormatter
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Configure Sentry
sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN', ''),
    integrations=[
        DjangoIntegration(),
        LoggingIntegration(
            level=logging.INFO,  # Capture info and above as breadcrumbs
            event_level=logging.ERROR  # Send errors as events
        ),
    ],
    traces_sample_rate=0.1,  # Adjust based on your traffic
    environment=os.environ.get('ENVIRONMENT', 'development'),
    send_default_pii=True,  # Include user information
)

# Configure structlog
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer(),
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

# Configure Django's logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            '()': jsonlogger.JsonFormatter,
            'format': '%(timestamp)s %(level)s %(name)s %(message)s',
        },
        'console': {
            '()': ColoredFormatter,
            'format': '%(log_color)s%(levelname)-8s%(reset)s [%(name)s] %(message)s',
            'log_colors': {
                'DEBUG': 'bg_cyan,fg_black',
                'INFO': 'bg_green,fg_black',
                'WARNING': 'bg_yellow,fg_black',
                'ERROR': 'bg_red,fg_white',
                'CRITICAL': 'bg_purple,fg_white',
            },
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'json_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'app.json'),
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10,
            'formatter': 'json',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'error.json'),
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10,
            'formatter': 'json',
        },
        'security_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'security.json'),
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10,
            'formatter': 'json',
        },
        'performance_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'performance.json'),
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
            'formatter': 'json',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'json_file'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['performance_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'app': {  # For your application code
            'handlers': ['console', 'json_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'performance': {  # For performance-related logs
            'handlers': ['console', 'performance_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'security': {  # For security-related logs
            'handlers': ['console', 'security_file'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}

# Create logs directory if it doesn't exist
os.makedirs(os.path.join(BASE_DIR, 'logs'), exist_ok=True)

# ...existing code...