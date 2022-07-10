from django.shortcuts import render
from .models import Movie

def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})
# Create your views here.
def info_page(request):
    return render(request,'info.html')