from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
                        CreateView,
                        UpdateView,
                        DeleteView,
                    )
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = "post-list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post-detail.html"

def home(request):
    return render(request, 'home.html')

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'author']    

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post-edit.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post-delete.html'
    success_url = reverse_lazy("post-list")  # Redirect to post list after deletion

