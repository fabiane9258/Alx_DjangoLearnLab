from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model. Validates that publication_year is not in the future.
    Fields: id, title, publication_year, author (author is stored as PK here).
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Ensure publication_year is not later than current year."""
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model and includes nested BookSerializer for related books.
    - books is read-only here and populated from Book.author (related_name='books').
    To support nested writes (create/update books with an author) you would
    implement custom create/update methods — not required for this task.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
