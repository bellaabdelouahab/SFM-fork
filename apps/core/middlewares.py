import time
import logging
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

logger = logging.getLogger(__name__)


class RequestTimingMiddleware(MiddlewareMixin):
    """
    Middleware to log the time taken to process each request.
    """
    def process_request(self, request):
        request.start_time = time.time()
        return None

    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            logger.info(f"Request to {request.path} took {duration:.2f}s")
        return response


class MaintenanceModeMiddleware(MiddlewareMixin):
    """
    Middleware to show maintenance page when MAINTENANCE_MODE setting is True.
    """
    def process_request(self, request):
        if getattr(settings, 'MAINTENANCE_MODE', False):
            from django.http import HttpResponse
            from django.template.loader import render_to_string
            
            # Admin users can still access the site
            if request.user.is_authenticated and request.user.is_staff:
                return None
                
            content = render_to_string('maintenance.html')
            return HttpResponse(content, status=503)
        return None
