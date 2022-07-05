from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(max_length=5000, verbose_name="Описание")
    image = models.ImageField(upload_to='movie', verbose_name="Постер")
    path_to_file = models.FilePathField(path="media/", verbose_name="Путь до файла")
    movie_id = models.UUIDField(primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "фильм"
        verbose_name_plural = "фильмы"
