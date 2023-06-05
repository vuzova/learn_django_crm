from django.shortcuts import render
from .models import *

# Create your views here.

def home(requst):
    return render(requst, 'home.html', context= {
        'list_articles' : Articles.objects.all(),
        'name': 'User'
    })