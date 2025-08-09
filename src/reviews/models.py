from django.db import models
from django.contrib.auth.models import User

from movies.models import Movie


class Review(models.Model):
    author = models.ForeignKey(User, verbose_name="Auteur", on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Film", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Titre", max_length=200, blank=True, null=True)
    date = models.DateField(verbose_name="Date de la critique", auto_now_add=True)
    update_date = models.DateField(verbose_name="Date de la dernière modification", auto_now=True)
    content = models.TextField(verbose_name="Contenu")
    published = models.BooleanField(verbose_name="Publiée", default=True)

    def __str__(self):
        return f"{self.movie} {self.date} {self.author}"
    
    class Meta:
        verbose_name = "Critique"
        verbose_name_plural = "Critiques"
        ordering = ("-date", "movie", "author")