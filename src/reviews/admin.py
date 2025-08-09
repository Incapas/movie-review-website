from django.contrib import admin

from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    empty_value_display = "Inconnu"
    list_display = ("id", "movie__title", "author__username", "published", "date", "update_date")
    list_editable = ("published",)
    list_per_page = 50
    search_fields = ("author", "movie")