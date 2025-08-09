from django import forms

class ReviewForm(forms.Form):
    title = forms.CharField(
        label="Titre",
        strip=True,
        required=True,
    )
    content = forms.CharField(
        label="Contenu",
        strip=True,
        required=True,
        widget=forms.Textarea()
        )
