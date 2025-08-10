from django.db import models

class Author(models.Model):
    """
    Author model:
    - name: author's full name.
    Relationship: One Author -> Many Books (reverse accessor: 'books').
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    - title: book title.
    - publication_year: integer year (positive).
    - author: ForeignKey to Author. related_name='books' makes Author.books available.
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
