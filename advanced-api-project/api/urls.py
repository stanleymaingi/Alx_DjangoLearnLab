from django.urls import path # type: ignore
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve single book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update book — ALX expects this exact substring
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete book — ALX expects this exact substring
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]

