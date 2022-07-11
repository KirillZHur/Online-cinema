from django.shortcuts import render
from .models import Movie


def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})
# Create your views here.


def info_page(request):
    return render(request, 'info.html')


def player(request, name):
    magnet_link = filter(lambda x: str(x.name).startswith(name), list(Movie.objects.all()))
    magnet_link = list(magnet_link).pop().magnet_link
    return render(request, 'player.html', {'magnet_link': magnet_link})
