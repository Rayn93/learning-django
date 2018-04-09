from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Autor, Book


# Create your views here.


class MainPageView(TemplateView):
    template_name = 'index.html'
    # def get(self, response, *args, **kwargs):
    #     return HttpResponse('OK')

# index_view = MainPageView.as_view()


class AuthorListView(ListView):
    model = Autor


class AuthorDetailView(DetailView):
    model = Autor


class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book