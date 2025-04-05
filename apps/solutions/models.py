from django.db import models 
from django.conf import settings 
from django.utils.translation import gettext_lazy as _ 
from apps.providers.models import Provider 
 
class Category(models.Model): 
    """Solution categories""" 
    name = models.CharField(max_length=100) 
    description = models.TextField(blank=True, null=True) 
    icon = models.CharField(max_length=50, blank=True, null=True) 
 
    class Meta: 
        verbose_name = _('Category') 
        verbose_name_plural = _('Categories') 
 
    def __str__(self): 
        return self.name 
 
class Solution(models.Model): 
    """Solution model for provider solutions""" 
    title = models.CharField(max_length=255) 
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='solutions') 
    categories = models.ManyToManyField(Category, related_name='solutions') 
    description = models.TextField() 
    features = models.TextField(blank=True, null=True) 
    price_type = models.CharField( 
        max_length=20, 
        choices=[ 
            ('free', 'Free'), 
            ('one_time', 'One-time payment'), 
            ('subscription', 'Subscription'), 
            ('custom', 'Custom pricing'), 
        ], 
        default='free' 
    ) 
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 
    image = models.ImageField(upload_to='solution_images', blank=True, null=True) 
    is_verified = models.BooleanField(default=False) 
    is_featured = models.BooleanField(default=False) 
    view_count = models.IntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
 
    class Meta: 
        verbose_name = _('Solution') 
        verbose_name_plural = _('Solutions') 
 
    def __str__(self): 
        return self.title 
 
class Review(models.Model): 
    """Reviews for solutions""" 
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name='reviews') 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) 
    comment = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
 
    class Meta: 
        verbose_name = _('Review') 
        verbose_name_plural = _('Reviews') 
        unique_together = ['solution', 'user'] 
 
    def __str__(self): 
        return f"{self.user.username}'s review of {self.solution.title}" 
