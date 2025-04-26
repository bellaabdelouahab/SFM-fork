# Django settings
import os
from dotenv import load_dotenv
from .logging import *

# Load environment variables from .env file
load_dotenv()

# Import settings based on environment
env = os.environ.get('DJANGO_ENV', 'development')

# pylint: disable=wrong-import-position
# flake8: noqa: E402
if env == 'production':
    from .production import *
elif env == 'test':
    from .test import *
else:
    from .development import *
