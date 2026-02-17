from rest_framework import serializers # type: ignore
from .models import Author, Book
from datetime import date

# Serializer for Book model with validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Ensure publication_year is not in the future
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for Author model with nested books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer for related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

class BookListView(generics.ListAPIView): # type: ignore
    serializer_class = BookSerializer
    permission_classes = [AllowAny] # type: ignore

    def get_queryset(self):
        queryset = Book.objects.all()
        author_name = self.request.query_params.get('author', None)
        if author_name:
            queryset = queryset.filter(author__name__icontains=author_name)
        return queryset

