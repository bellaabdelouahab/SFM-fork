from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        """Send email using the form data"""
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = f"Message from {name} ({email}):\n\n{self.cleaned_data['message']}"
        
        send_mail(
            subject=f"Contact Form: {subject}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
        )
