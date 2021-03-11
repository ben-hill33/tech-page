from django.urls import path
from .views import *

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("content/<int:pk>/detail/", PostDetailView.as_view(), name="post_detail"),
    path("content/new/", PostCreateView.as_view(), name="new_post"),
    path("content/<int:pk>/edit/", PostUpdateView.as_view(), name="update_post"),
    path("content/<int:pk>/delete/", PostDeleteView.as_view(), name="delete_post"),
]