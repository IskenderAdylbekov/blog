from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog Page'
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
