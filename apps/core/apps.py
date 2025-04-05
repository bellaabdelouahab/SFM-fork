from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Core'

    def ready(self):
        """
        Perform initialization tasks when Django starts.
        """
        # Import the checks module to register system checks
        from . import checks  # noqa
