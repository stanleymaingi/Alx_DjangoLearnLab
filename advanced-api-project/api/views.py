from rest_framework import generics # type: ignore
from rest_framework.permissions import IsAuthenticated, AllowAny # type: ignore
from .models import Book
from .serializers import BookSerializer

# List all books - open to anyone
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # anyone can view

# Retrieve single book by ID - open to anyone
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

# Create a new book - authenticated users only
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Update an existing book - authenticated users only
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete a book - authenticated users only
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



# BookListView: Lists all books, accessible by anyone
# BookDetailView: Retrieves details of a single book by ID, accessible by anyone
# BookCreateView: Creates a new book, requires authentication
# BookUpdateView: Updates a book, requires authentication
# BookDeleteView: Deletes a book, requires authentication
