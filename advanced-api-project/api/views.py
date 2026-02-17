from rest_framework import generics, filters # type: ignore
from rest_framework.permissions import IsAuthenticated, AllowAny # type: ignore
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from .models import Book
from .serializers import BookSerializer

# List all books with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # public access

    # Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields for filtering using ?field=value
    filterset_fields = ['title', 'publication_year', 'author__name']

    # Fields for search using ?search=keyword
    search_fields = ['title', 'author__name']

    # Fields for ordering using ?ordering=field
    ordering_fields = ['title', 'publication_year', 'author__name']

    # Default ordering
    ordering = ['title']



# Retrieve single book (read-only for anyone)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

# Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Update an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
