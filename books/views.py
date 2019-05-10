from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from books.models import Book


class BookList(ListView):
    model = Book
    template_name = 'books/book_list.html'


class BookView(DetailView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = Book
    template_name = 'books/book_edit.html'
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy('book_list')