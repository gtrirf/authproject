from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Author, BooksAuthor, Books, BookCategory, Review
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView


class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'
    context_object_name = 'book'


class BookDetailView(DetailView):
    model = Books
    template_name = 'book_detail.html'


class BookCreateView(CreateView):
    model = Books
    template_name = 'book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('books:book_list')


class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('books:book_list')

