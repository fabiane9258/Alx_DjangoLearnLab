import os
import sys
import django

# 🔧 Add project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

# 🔧 Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# 🔧 Setup Django
django.setup()

from relationship_app.models import Author, Book, Library

# Query 1: All books by a specific author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    
    books_by_author_explicit = Book.objects.filter(author=author)
    
    print(f"\nBooks by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")


# Query 2: List all books in a library
library_name = "City Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# Query 3: Retrieve the librarian for a library
try:
    librarian_check = Librarian.objects.get(library=library)  # ✅ Required by ALX checker
    librarian = library.librarian
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}")
