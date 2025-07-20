from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book  # ✅ This must be included

# ✅ Class-based view to show library details and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Your template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # ✅ Books available in that library
        return context

# ✅ Optional: function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # ✅ Must be present
    return render(request, 'relationship_app/list_books.html', {'books': books})
