from django.shortcuts import render
from .models import *

# Create your views here.

def home(requst):
    return render(requst, 'home.html', context= {
        'list_articles' : Articles.objects.all(),
        'name': 'User'
    })

def page(request, id):
    return render(request, 'page.html', context = {
        'article': Articles.objects.get(id=id)
    })