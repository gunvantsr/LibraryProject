from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='books/covers/', default='book.png')
    book_file = models.FileField(upload_to='books/files/', max_length=100)

    def __str__(self):
        return self.title