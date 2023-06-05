from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

class HomeListView(ListView):
    model = Articles
    template_name = 'home.html'
    context_object_name = "list_articles"

class HomeDetailView(DetailView):
    model = Articles
    template_name = 'page.html'
    context_object_name = 'article'