import re
import string

from django import forms
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur",
        required=True,
        min_length=6,
        max_length=50
        )
    password = forms.CharField(
        label="Mot de passe",
        required=True,
        min_length=10,
        widget=forms.PasswordInput()
        )
    
class SignupForm(UserForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        verification = re.findall(r"[^a-zA-Z0-9]", username)
        if not verification:
            return username
        raise ValidationError("Le nom d'utilisateur ne peut contenir que des chiffes, des lettres et des '_'")
    
    def clean_password(self):
        UPPERCASE_LETTERS = [*string.ascii_uppercase]
        LOWERCASE_LETTERS = [*string.ascii_lowercase]
        DIGITS = [*string.digits]
        PUNCTUATION = [*string.punctuation]

        verification = {}.fromkeys(("majuscule", "minuscule", "chiffre", "ponctuation"))

        password = self.cleaned_data["password"]

        for char in password:
            if char in UPPERCASE_LETTERS:
                verification["majuscule"] = True
            elif char in LOWERCASE_LETTERS:
                verification["minuscule"] = True
            elif char in DIGITS:
                verification["chiffre"] = True
            elif char in PUNCTUATION:
                verification["ponctuation"] = True
        
        if all(verification.values()):
                return password
        raise ValidationError("Le mot de passe doit contenir au moins : 1 majuscule, 1 minuscule, 1 chiffre, 1 caractère spécial !")

class LoginForm(UserForm):
    pass