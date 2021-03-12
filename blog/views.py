from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from django.utils import timezone
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

    def get_queryset(self):
        return Post.objects.filter(published_date=timezone.now).order_by(
            "published_date"
        )


class PostDetailView(DetailView):
    template_name = "posts/post_detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "posts/new_post.html"
    model = Post
    fields = ["author", "title", "text"]


class PostUpdateView(UpdateView):
    template_name = "posts/update_post.html"
    model = Post
    fields = ["title", "text"]


class DraftListView(ListView):
    template_name = "posts/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by("created_date")


class PostDeleteView(DeleteView):
    template_name = "posts/delete_post.html"
    model = Post
    success_url = reverse_lazy("post_list")


@login_required
def post_published(pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("post_detail", pk=pk)
