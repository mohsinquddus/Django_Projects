from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movies
from datetime import datetime
# Create your views here.
def index(request):
     return HttpResponse("Hello Movies")
    
def displaymovies(request):
    #  Select * from Movies
    movies =Movies.objects.all()
    # output = ', '.join([m.title for m in movies])
    #  Select * from Movies Where ...
    # Movies.obects.filter(year=1984)
    # Movies.object.get(id=1)
    # return HttpResponse(output)
    # print(movies[0].title)
    return render(request,'movies/displaymovies.html',{'movies':movies})

def detail(request,movie_id):
    # movie = Movies.objects.get(pk=movie_id)
    movie = get_object_or_404(Movies, pk=movie_id)
    return render(request, "movies/detail.html",{'movie':movie})