import re
import magic
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_file_size(value, max_size=5242880):  # 5MB default
    """
    Validate that the file size is under the specified limit.
    """
    if value.size > max_size:
        raise ValidationError(
            _('File too large. Size cannot exceed %(size)s MB.'),
            params={'size': max_size / 1024 / 1024},
        )


def validate_file_type(value, allowed_types=None):
    """
    Validate file mimetype using python-magic.
    Default allowed types: PDF, DOCX, XLSX, PNG, JPEG, JPG.
    """
    if allowed_types is None:
        allowed_types = [
            'application/pdf',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'image/png',
            'image/jpeg',
        ]
    
    # Get MIME type
    file_type = magic.from_buffer(value.read(1024), mime=True)
    value.seek(0)  # Reset file pointer
    
    if file_type not in allowed_types:
        raise ValidationError(
            _('Unsupported file type. Allowed types are: %(types)s'),
            params={'types': ', '.join(allowed_types)},
        )


def validate_phone_number(value):
    """
    Validate phone number format.
    Accepts formats like: +1234567890, 123-456-7890, (123) 456-7890
    """
    pattern = r'^\+?1?\d{9,15}$|^\(\d{3}\)\s?\d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$'
    if not re.match(pattern, value):
        raise ValidationError(
            _('Enter a valid phone number.')
        )


def validate_moroccan_phone_number(value):
    """
    Validate Moroccan phone number format.
    Valid formats: 06XXXXXXXX, 07XXXXXXXX, +212XXXXXXXX
    """
    pattern = r'^(0[67]\d{8}|\+212[67]\d{8})$'
    if not re.match(pattern, value):
        raise ValidationError(
            _('Enter a valid Moroccan phone number.')
        )


def validate_password_strength(value):
    """
    Validate that the password meets minimum strength requirements.
    - At least 8 characters
    - Contains at least 1 uppercase letter
    - Contains at least 1 lowercase letter
    - Contains at least 1 digit
    - Contains at least 1 special character
    """
    if len(value) < 8:
        raise ValidationError(
            _('Password must be at least 8 characters long.')
        )
    
    if not re.search(r'[A-Z]', value):
        raise ValidationError(
            _('Password must contain at least one uppercase letter.')
        )
    
    if not re.search(r'[a-z]', value):
        raise ValidationError(
            _('Password must contain at least one lowercase letter.')
        )
    
    if not re.search(r'\d', value):
        raise ValidationError(
            _('Password must contain at least one digit.')
        )
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError(
            _('Password must contain at least one special character.')
        )
