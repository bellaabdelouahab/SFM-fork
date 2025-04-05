# Django settings
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import settings based on environment
env = os.environ.get('DJANGO_ENV', 'development')

if env == 'production':
    from .production import *
elif env == 'test':
    from .test import *
else:
    from .development import *
