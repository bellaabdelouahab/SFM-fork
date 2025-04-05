from django.urls import path
from . import views

app_name = 'solutions'

urlpatterns = [
    # List view
    path('', views.SolutionListView.as_view(), name='solution_list'),
    
    # Detail view
    path('<int:pk>/', views.SolutionDetailView.as_view(), name='solution_detail'),
    
    # Category views
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
]
