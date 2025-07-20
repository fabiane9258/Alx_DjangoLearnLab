from django.shortcuts import render, get_object_or_404
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Function-based view to show details of a library
def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'library_detail.html', {'library': library})
