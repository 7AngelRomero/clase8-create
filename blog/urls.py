from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]