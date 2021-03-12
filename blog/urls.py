from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("content/<int:pk>/detail/", PostDetailView.as_view(), name="post_detail"),
    path("content/new/", PostCreateView.as_view(), name="new_post"),
    path("content/<int:pk>/edit/", PostUpdateView.as_view(), name="update_post"),
    path("drafts/", DraftListView.as_view(), name="post_draft_list"),
    path("content/<int:pk>/publish/", views.post_published, name="post_publish"),
    path("content/<int:pk>/delete/", PostDeleteView.as_view(), name="delete_post"),
]