from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    template_name = "post-list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post-detail.html"

def home(request):
    return render(request, 'home.html')