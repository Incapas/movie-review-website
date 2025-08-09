from django.db import models


class Director(models.Model):
    forename = models.CharField(verbose_name="Prénom", max_length=150, blank=True)
    lastname = models.CharField(verbose_name="Nom", max_length=150, blank=True)

    def __str__(self):
        return f"{self.forename} {self.lastname}"
    
    class Meta:
        verbose_name = "Réalisateur/trice"
        verbose_name_plural = "Réalisateur/trice(s)"
        ordering = ("lastname", "forename") 


class Gender(models.Model):
    label = models.CharField(verbose_name="Genre", max_length=150)

    def __str__(self):
        return f"{self.label}"
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ("label",)


class Country(models.Model):
    label = models.CharField(verbose_name="Pays", max_length=150)

    def __str__(self):
        return f"{self.label}"

    class Meta:
        verbose_name = "Pays"
        verbose_name_plural = "Pays"
        ordering = ("label",)


class Movie(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=150, blank=True, null=True)
    synopsis = models.TextField(verbose_name="Synopsis", blank=True, null=True)
    direction = models.ManyToManyField(Director, verbose_name="Réalisateur/trice(s)", blank=True)
    country_of_production = models.ManyToManyField(Country, verbose_name="Pays de production", blank=True)
    gender = models.ManyToManyField(Gender, verbose_name="Genre(s)", blank=True)
    duration = models.IntegerField(verbose_name="Durée (en minutes)", blank=True, null=True)
    release_year = models.IntegerField(verbose_name="Année de sortie en France", blank=True, null=True)

    def __str__(self):
        return f"{self.title} de {self.release_year}"
    
    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"
        ordering = ("title", "-release_year")