from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Create an author
        self.author = Author.objects.create(name="Author One")
        
        # Create some books
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author)

        # URL for the book list
        self.list_url = reverse('book-list')  # adjust according to your urls.py name
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])  # detail view URL function
        self.create_url = reverse('book-create')
        self.update_url = lambda pk: reverse('book-update', args=[pk])
        self.delete_url = lambda pk: reverse('book-delete', args=[pk])

    def test_book_list_readable_by_all(self):
        """Anyone can view the book list"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_book_detail_readable_by_all(self):
        """Anyone can view a book detail"""
        response = self.client.get(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Book One")

    def test_create_book_requires_authentication(self):
        """Unauthenticated users cannot create a book"""
        data = {"title": "New Book", "publication_year": 2022, "author": self.author.pk}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticated user can create
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_requires_authentication(self):
        """Unauthenticated users cannot update a book"""
        data = {"title": "Updated Title"}
        response = self.client.put(self.update_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.login(username='testuser', password='testpass')
        data = {"title": "Updated Title", "publication_year": 2020, "author": self.author.pk}
        response = self.client.put(self.update_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_requires_authentication(self):
        """Unauthenticated users cannot delete a book"""
        response = self.client.delete(self.delete_url(self.book2.pk))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.delete_url(self.book2.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """Filter books by title"""
        response = self.client.get(self.list_url, {'title': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_search_books_by_author(self):
        """Search books by author name"""
        response = self.client.get(self.list_url, {'search': 'Author One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year(self):
        """Order books by publication_year descending"""
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)
