from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Autor



# Create your views here.

class AuthorListView(ListView):
    model = Autor

