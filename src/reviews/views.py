from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Review
from .forms import ReviewForm
from movies.models import Movie



def reviews(request, pk):
    reviews = Review.objects.filter(movie_id=pk)
    return render(request, "reviews/reviews.html", context={"reviews": reviews})

def review(request, pk):
    review = Review.objects.get(pk=pk)
    return render(request, "reviews/review.html", context={"review": review})

@login_required
def write_review(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            Review.objects.create(author=user, movie=movie, title=title, content=content)
            return redirect("movies")
    else:
        form = ReviewForm()
    return render(request, "reviews/write.html", context={"movie": movie, "form": form})

@login_required
def update_review(request, pk):
    review = Review.objects.get(pk=pk)
    if review.author.pk != request.user.pk:
        return HttpResponse("Vous n'avez pas l'autorisation d'accéder à cette page.")
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            review.title = title
            review.content = content
            review.save()
            return redirect("user_profile")
    else:
        initial_data = {"title": review.title, "content": review.content}
        form = ReviewForm(initial=initial_data) 
    return render(request, "reviews/update.html", context={"form": form})

@login_required
def delete_review(request, pk):
    review = Review.objects.get(pk=pk)
    if review.author.pk != request.user.pk:
        return HttpResponse("Vous n'avez pas l'autorisation d'accéder à cette page.")
    if request.method == "POST":
        Review.objects.get(pk=pk).delete()
        return redirect("user_profile")
    return render(request, "reviews/delete.html")