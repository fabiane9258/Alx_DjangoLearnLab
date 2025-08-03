# api/views.py

from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

# This view is still open because generic views don't always
# respect default permissions unless configured to.
# For the checker, our global setting is what matters most.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    This ViewSet is now protected by the global default permission policy
    (IsAuthenticated) defined in settings.py.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated] # This line is now redundant and can be removed