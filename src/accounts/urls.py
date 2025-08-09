from django.urls import path

from .views import user_registration, user_login, user_logout, user_profile

urlpatterns = [
    path('inscription/', user_registration, name="user_registration"),
    path('connexion/', user_login, name="user_login"),
    path('deconnexion/', user_logout, name="user_logout"),
    path('profil/', user_profile, name="user_profile")
]