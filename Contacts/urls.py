from django.contrib import admin
from django.urls import path, include
from .views import index, insert, display

app_name = 'contacts'

urlpatterns = [
    path('display', display, name='insert'),
    path('insert', insert, name='insert'),
    path('', index, name='index'),

]
