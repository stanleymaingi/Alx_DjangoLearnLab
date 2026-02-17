from rest_framework import generics # type: ignore
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets # type: ignore
from rest_framework.permissions import IsAuthenticated, IsAdminUser # type: ignore


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
   