from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Provider(models.Model):
    """Provider model for solution providers"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='provider')
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='provider_logos', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    subscription_status = models.CharField(
        max_length=20,
        choices=[
            ('free', 'Free'),
            ('basic', 'Basic'),
            ('premium', 'Premium'),
        ],
        default='free'
    )
    subscription_expiry = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _('Provider')
        verbose_name_plural = _('Providers')
    def __str__(self):
        return self.company_name
