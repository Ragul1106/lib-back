from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, author_list_create, author_detail

urlpatterns = [
    # Books
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),

    # Authors
    path('authors/', author_list_create, name='author-list-create'),
    path('authors/<int:pk>/', author_detail, name='author-detail'),
]
