from django import forms
from .models import Book


class ExampleForm(forms.Form):
    """
    Example secure form demonstrating validation and CSRF protection.
    """

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name.isalpha():
            raise forms.ValidationError("Name must contain only letters.")
        return name


class BookForm(forms.ModelForm):
    """
    Secure ModelForm for Book model.
    """

    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]

    def clean_publication_year(self):
        year = self.cleaned_data.get("publication_year")
        if year < 0:
            raise forms.ValidationError("Publication year must be positive.")
        return year
