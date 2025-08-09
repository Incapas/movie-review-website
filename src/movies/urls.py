from django.urls import path

from .views import movies_list

urlpatterns = [
    path('', movies_list, name="movies"),
]