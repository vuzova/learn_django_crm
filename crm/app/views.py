from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

class HomeListView(ListView):
    model = Articles
    template_name = 'home.html'
    context_object_name = "list_articles"

    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Админ"  # здесь указать нужное имя
        return context

class HomeDetailView(DetailView):
    model = Articles
    template_name = 'page.html'
    context_object_name = 'article'

def create(request):
    return render(request, 'create.html')