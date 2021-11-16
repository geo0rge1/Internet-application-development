from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PCSDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='reviews-home'),
    path('about/', views.about, name='reviews-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='reviews-detail'),
    path('PCS/', views.pcs, name='reviews-pc'),
    path('pc/<int:pk>/', PCSDetailView.as_view(), name='reviews-pcs_about'),
    
    
]
