from django.shortcuts import render, get_object_or_404
from .models import Book, Library

# View to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# View to display details of a specific library
def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'relationship_app/library_detail.html', {'library': library})
