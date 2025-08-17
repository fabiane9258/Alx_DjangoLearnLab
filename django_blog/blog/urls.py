from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,
    SearchResultsView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),  # ✅ Tag filter
    path('search/', SearchResultsView.as_view(), name='search-results'),  # ✅ Search
]
