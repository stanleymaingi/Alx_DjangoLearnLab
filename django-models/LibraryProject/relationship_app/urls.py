from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # Function-based view: list all books
    path("books/", views.list_books, name="list_books"),
    
    # Class-based view: detail of a library by ID
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]