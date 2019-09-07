from django import forms
from .models import Books

class BookUploadForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ['title', 'author','cover', 'book_file']