from django.urls.base import reverse_lazy
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class PostListView(ListView):
    template_name = "posts/post_list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/post_detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "posts/new_post.html"
    model = Post


class PostUpdateView(UpdateView):
    template_name = "posts/update_post.html"
    model = Post
    fields = ["title", "text"]


class PostDeleteView(DeleteView):
    template_name = "posts/delete_post.html"
    model = Post
    success = reverse_lazy("post_list.html")
