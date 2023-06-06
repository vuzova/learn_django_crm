
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('page/<int:pk>', HomeDetailView.as_view(), name='page'),
    path('create', create, name='create')
]
