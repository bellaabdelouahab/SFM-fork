import uuid
import logging
import structlog

logger = structlog.get_logger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Generate a unique request ID
        request_id = str(uuid.uuid4())
        request.request_id = request_id  # Add to request object for access elsewhere
        
        # Add request data to log context
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(
            request_id=request_id,
            user_id=request.user.id if hasattr(request, 'user') and request.user.is_authenticated else None,
            user_email=request.user.email if hasattr(request, 'user') and request.user.is_authenticated else None,
            path=request.path,
            method=request.method,
            ip_address=self._get_client_ip(request)
        )
        
        logger.debug("Request started")
        
        response = self.get_response(request)
        
        # Log response details
        structlog.contextvars.bind_contextvars(
            status_code=response.status_code,
        )
        logger.debug("Request finished")
        
        return response
        
    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def process_exception(self, request, exception):
        logger.exception("Unhandled exception", exc_info=exception)
        return None
