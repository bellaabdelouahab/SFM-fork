from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact_success')
    
    def form_valid(self, form):
        # Process the form data
        form.send_email()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    """View for displaying a success message after contact form submission"""
    template_name = 'pages/contact_success.html'
