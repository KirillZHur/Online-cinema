from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(max_length=5000, verbose_name="Описание")
    image = models.ImageField(upload_to='movie', verbose_name="Постер")
    magnet_link = models.CharField(max_length=500,primary_key=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "фильм"
        verbose_name_plural = "фильмы"
