from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian
from django.views.generic.detail import DetailView
from .models import Library


# ---------------------------
# Function-based view
# ---------------------------
def list_books(request):
    """
    Lists all books in the database using the correct template path.
    """
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    """
    Displays details for a specific library,
    including all books in that library.
    """
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books for this library to the context
        context['books'] = self.object.book_set.all()  # assumes Book has a FK to Library
        return context