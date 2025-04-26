import os

from django.core.exceptions import ImproperlyConfigured


def get_env_list(var_name, default=None):
    value = os.environ.get(var_name, default)
    if value is None:
        raise ImproperlyConfigured(f"{var_name} environment variable is not set.")
        
    return value.split(",")
