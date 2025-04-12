import time
import functools
import structlog
import logging

# Standard loggers
app_logger = structlog.get_logger('app')
security_logger = structlog.get_logger('security')
performance_logger = structlog.get_logger('performance')

def get_logger(name=None):
    """Get a structured logger with the given name."""
    if name:
        return structlog.get_logger(name)
    return app_logger

def log_timing(func=None, *, level='INFO', logger=None):
    """
    Decorator to log the execution time of a function.
    
    Usage:
      @log_timing
      def my_function():
          ...
      
      @log_timing(level='DEBUG', logger=custom_logger)
      def another_function():
          ...
    """
    actual_decorator = _make_timing_decorator(level=level, logger=logger)
    
    if func is None:
        return actual_decorator
    return actual_decorator(func)

def _make_timing_decorator(level='INFO', logger=None):
    if logger is None:
        logger = performance_logger
    
    log_level = getattr(logging, level.upper(), logging.INFO)
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed_time = (time.time() - start_time) * 1000  # ms
            
            logger.log(
                log_level,
                f"{func.__module__}.{func.__name__} execution time",
                execution_time_ms=elapsed_time,
                function=f"{func.__module__}.{func.__name__}"
            )
            return result
        return wrapper
    return decorator
