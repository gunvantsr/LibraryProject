from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('',views.index, name="home"),
    path('books/', views.books_list, name='books_list'),
    path('books/upload', views.books_upload, name='books_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
