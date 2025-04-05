import os
import uuid
import hashlib
from functools import wraps
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
import redis
from django.conf import settings


def get_client_ip(request):
    """
    Get the client's IP address from the request.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def unique_slug_generator(instance, field_name, new_slug=None):
    """
    Generate a unique slug for a model instance.
    If new_slug is provided, use that, otherwise use the value of field_name.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(getattr(instance, field_name))

    model = instance.__class__
    slug_exists = model.objects.filter(slug=slug).exists()
    
    if slug_exists:
        # If slug already exists, add a timestamp
        slug = f"{slug}-{int(timezone.now().timestamp())}"
    
    return slug


def paginate_queryset(request, queryset, per_page=10):
    """
    Helper function to paginate a queryset
    """
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, per_page)
    
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    return paginated_queryset


def generate_file_path(instance, filename, path='uploads'):
    """
    Generate a unique file path for uploaded files.
    """
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join(path, filename)


def timed_cache(timeout=300):
    """
    Timed cache decorator using Redis for storage
    """
    
    # Get Redis connection from Django settings or use default
    redis_instance = redis.Redis(
        host=getattr(settings, 'REDIS_HOST', 'localhost'),
        port=getattr(settings, 'REDIS_PORT', 6379),
        db=getattr(settings, 'REDIS_DB', 0),
        password=getattr(settings, 'REDIS_PASSWORD', None)
    )
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate a unique key based on function name and arguments
            key = f"cache:{func.__module__}:{func.__name__}:{str(args)}:{str(kwargs)}"
            key_hash = hashlib.md5(key.encode()).hexdigest()
            
            # Try to get from Redis cache
            cached = redis_instance.get(key_hash)
            if cached:
                return eval(cached.decode())  # Convert from bytes to Python object
            
            # Call the function and store result in Redis
            result = func(*args, **kwargs)
            redis_instance.setex(
                key_hash, 
                timeout,  # Redis takes seconds directly
                str(result)  # Simple serialization
            )
            return result
        
        return wrapper
    
    return decorator
