import uuid

from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    movie_id = uuid.uuid4()
