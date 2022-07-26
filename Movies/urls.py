from django.contrib import admin
from django.urls import path, include
from .views import index, displaymovies, detail

app_name = 'movies'

urlpatterns = [
    path('', index, name='index'),
    path('displaymovies', displaymovies, name='displaymovies'),
    path('detail/<int:movie_id>',detail,name="movie_detail"),

]