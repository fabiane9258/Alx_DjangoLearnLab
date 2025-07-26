from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('relationship_app.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('relationship_app.can_create_book', raise_exception=True)
def book_create(request):
    # your logic to create a book
    pass

@permission_required('relationship_app.can_edit_book', raise_exception=True)
def book_edit(request, book_id):
    # your logic to edit a book
    pass

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def book_delete(request, book_id):
    # your logic to delete a book
    pass
