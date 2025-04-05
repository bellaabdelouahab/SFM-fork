from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin to require that the user is a staff member.
    """
    permission_denied_message = _("You do not have permission to access this page.")
    
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()


class OwnershipRequiredMixin:
    """
    Mixin to require that the user is the owner of the object.
    Override get_owner_field() to specify the field that represents the owner.
    """
    owner_field = 'user'  # Default field name for the owner
    
    def get_owner_field(self):
        return self.owner_field
        
    def test_func(self):
        obj = self.get_object()
        owner_field = self.get_owner_field()
        return getattr(obj, owner_field) == self.request.user


class AuditMixin:
    """
    Mixin to automatically set created_by and updated_by fields on save.
    """
    def save(self, *args, **kwargs):
        if not self.pk and hasattr(self, 'created_by') and hasattr(self, 'request'):
            self.created_by = self.request.user
        if hasattr(self, 'updated_by') and hasattr(self, 'request'):
            self.updated_by = self.request.user
        super().save(*args, **kwargs)
