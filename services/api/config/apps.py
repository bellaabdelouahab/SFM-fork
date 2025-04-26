from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class AppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config'
    verbose_name = 'config'

    def ready(self):
        """
        Perform initialization tasks when Django starts.
        """
        # Database creation is now handled in settings initialization
        logger.info("Application is ready")
