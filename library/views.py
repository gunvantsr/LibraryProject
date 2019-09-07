from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import BookUploadForm
from .models import Books

# Create your views here.
def index(request):
    return render(request, 'library/home.html')

def books_list(request):
    books = Books.objects.all()
    return render(request, 'library/books_list.html', {'books':books})

def books_upload(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookUploadForm()
        return render(request, 'library/books_upload.html', {'form': form})