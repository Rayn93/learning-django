from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Autor, Book


# Create your views here.

class AuthorListView(ListView):
    model = Autor


class AuthorDetailView(DetailView):
    model = Autor


class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book