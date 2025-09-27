from django.urls import path
from .views import ( PostListView,
                    PostDetailView, 
                    PostCreateView,
                    PostUpdateView 
                    )
from . import views

urlpatterns = [ # lista de funciones que se pueden llamar desde la ur
    path('', views.home, name='home'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
]