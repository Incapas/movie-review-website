from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from django.http import HttpResponse

from .forms import SignupForm, LoginForm
from reviews.models import Review


def user_registration(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
            except IntegrityError:
                return HttpResponse("Nom d'utilisateur déjà existant")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", context={"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user_profile")
        else:
            return redirect("user_login")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", context={"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("user_login")

@login_required
def user_profile(request):
    user = request.user
    reviews = Review.objects.filter(author_id=user.pk)
    return render(request, "accounts/profile.html", context={"reviews": reviews, "user": user})