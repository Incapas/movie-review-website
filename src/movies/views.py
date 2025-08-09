from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Movie
from .forms import SearchForm


def movies_list(request):
    movies = Movie.objects.all()

    paginator = Paginator(movies, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if title:
                page_obj = Movie.objects.filter(title__icontains=title)
            else:
                page_obj = page_obj
    else:
        form = SearchForm()
    return render(request, "movies/index.html", context={"form": form, "page_obj": page_obj})


