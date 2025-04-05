import os
import uuid
import hashlib
from functools import wraps
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.utils.text import slugify


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
    Simple timed cache decorator for functions
    """
    cache = {}
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            key_hash = hashlib.md5(key.encode()).hexdigest()
            
            if key_hash in cache:
                result, timestamp = cache[key_hash]
                if timestamp + timeout > timezone.now().timestamp():
                    return result
            
            result = func(*args, **kwargs)
            cache[key_hash] = (result, timezone.now().timestamp())
            return result
        
        return wrapper
    
    return decorator
