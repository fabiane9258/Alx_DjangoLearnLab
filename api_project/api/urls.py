# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet # Import both the old and new view

# Create a router instance
router = DefaultRouter()

# Register the BookViewSet with the router
# The URL prefix will be 'books_all'
router.register(r'books_all', BookViewSet, basename='book_all')

# The API URLs are now determined automatically by the router.
# We also keep the old path for the BookList view as requested.
urlpatterns = [
    # Route for the original BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]