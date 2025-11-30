from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Read-only views (accessible by everyone)
class BookListView(generics.ListAPIView):
    """
    Lists all books.
    Anyone can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Everyone can view

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    Anyone can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Everyone can view

# Write views (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Only authenticated users can access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only authenticated users can access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Only authenticated users can access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# BookListView: Lists all books. Read-only, open to everyone.
# BookDetailView: Retrieves a single book by ID. Read-only.
# BookCreateView: Creates a new book. Only authenticated users.
# BookUpdateView: Updates an existing book. Only authenticated users.
# BookDeleteView: Deletes a book. Only authenticated users.
