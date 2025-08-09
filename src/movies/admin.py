from django.contrib import admin

from .models import Director, Gender, Country, Movie


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("id", "forename", "lastname")
    list_editable = ("forename", "lastname")
    search_fields = ("lastname",)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ("id", "label",)
    list_editable = ("label",)
    search_fields = ("label",)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "label",)
    list_editable = ("label",)
    search_fields = ("label",)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    autocomplete_fields = ("direction", "country_of_production", "gender")
    list_display = ("id", "title", "release_year")
    list_editable = ("title", "release_year")
    search_fields = ("title", "release_year")