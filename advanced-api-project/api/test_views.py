# api/test_views.py
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create authors and books
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')

        self.book1 = Book.objects.create(title='Book One', publication_year=2001, author=self.author1)
        self.book2 = Book.objects.create(title='Book Two', publication_year=2005, author=self.author2)

        self.books_url = '/api/books/'

    def test_list_books(self):
        """Anyone can list books"""
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Anyone can retrieve a single book"""
        url = f'{self.books_url}{self.book1.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book One')

    def test_create_book_requires_authentication(self):
        """Unauthenticated users cannot create books"""
        data = {
            'title': 'Book Three',
            'publication_year': 2010,
            'author': self.author1.id
        }
        response = self.client.post(self.books_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):
        """Authenticated users can create books"""
        self.client.login(username='testuser', password='testpass')
        data = {
            'title': 'Book Three',
            'publication_year': 2010,
            'author': self.author1.id
        }
        response = self.client.post(self.books_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_requires_authentication(self):
        """Unauthenticated users cannot update books"""
        url = f'{self.books_url}{self.book1.id}/'
        response = self.client.patch(url, {'title': 'Updated Title'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_update_book(self):
        """Authenticated users can update books"""
        self.client.login(username='testuser', password='testpass')
        url = f'{self.books_url}{self.book1.id}/'
        response = self.client.patch(url, {'title': 'Updated Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_authenticated_user_can_delete_book(self):
        """Authenticated users can delete books"""
        self.client.login(username='testuser', password='testpass')
        url = f'{self.books_url}{self.book1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Can filter books by author id"""
        response = self.client.get(f'{self.books_url}?author={self.author1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author1.id)

    def test_search_books_by_title(self):
        """Can search books by title"""
        response = self.client.get(f'{self.books_url}?search=Book One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_order_books_by_year(self):
        """Can order books by publication_year"""
        response = self.client.get(f'{self.books_url}?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
