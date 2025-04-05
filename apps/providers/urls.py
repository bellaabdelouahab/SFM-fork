from django.urls import path
from . import views

app_name = 'providers'

urlpatterns = [
    # List view
    path('', views.ProviderListView.as_view(), name='provider_list'),
    
    # Detail view
    path('<int:pk>/', views.ProviderDetailView.as_view(), name='provider_detail'),
]
