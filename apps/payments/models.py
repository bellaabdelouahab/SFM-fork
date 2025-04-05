from django.db import models 
from django.conf import settings 
from django.utils.translation import gettext_lazy as _ 
 
class Subscription(models.Model): 
    """Provider subscription plans""" 
    name = models.CharField(max_length=100) 
    description = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    duration_days = models.IntegerField() 
    features = models.TextField() 
    is_active = models.BooleanField(default=True) 
 
    class Meta: 
        verbose_name = _('Subscription') 
        verbose_name_plural = _('Subscriptions') 
 
    def __str__(self): 
        return self.name 
 
class Payment(models.Model): 
    """Payment records""" 
    PAYMENT_STATUS_CHOICES = [ 
        ('pending', 'Pending'), 
        ('completed', 'Completed'), 
        ('failed', 'Failed'), 
        ('refunded', 'Refunded'), 
    ] 
 
    PAYMENT_TYPE_CHOICES = [ 
        ('subscription', 'Subscription'), 
        ('solution', 'Solution Purchase'), 
        ('ai_idea', 'AI Idea Purchase'), 
    ] 
 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments') 
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES) 
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending') 
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True) 
    transaction_id = models.CharField(max_length=255, blank=True, null=True) 
    payment_method = models.CharField(max_length=100, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
 
    class Meta: 
        verbose_name = _('Payment') 
        verbose_name_plural = _('Payments') 
 
    def __str__(self): 
        return f"{self.user.username} - {self.amount} - {self.payment_type}" 
