from django.urls import path
from .views import *

app_name = 'books'
urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('create/', BookCreateView.as_view(), name='create_book')
]
