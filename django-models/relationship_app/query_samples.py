import os
import django # type: ignore

# Set Django environment for standalone script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.first()  # or filter by name: Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books_by_author:
    print(f"- {book.title}")

# 2. List all books in a library
library = Library.objects.first()
books_in_library = library.books.all()
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian of {library.name}: {librarian.name}")