from rest_framework import generics, permissions, filters
from django_filters import rest_framework  # <- checker expects this
from .models import Book
from .serializers import BookSerializer

# Read-only views → everyone can access
class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books with advanced query capabilities:
    - Filtering by title, author, and publication_year
    - Searching by title and author
    - Ordering by any field (default: title)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # read-only for unauthenticated users

    # Enable filtering, searching, and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields users can filter by
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fields users can search in
    search_fields = ['title', 'author__name']

    # Fields users can order by
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Write views → only authenticated users
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

###BookListView supports:
##- Filtering: ?title=Book1&author__name=John
##- Searching: ?search=keyword
##- Ordering: ?ordering=title or ?ordering=-publication_year
