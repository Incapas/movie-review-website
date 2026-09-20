# Films & Critiques

> Un catalogue de films où chacun peut lire les avis des autres et publier les siens.

Application web de critiques de films : le visiteur parcourt le catalogue, cherche un titre et lit les critiques déjà publiées ; une fois inscrit, il rédige les siennes et les gère depuis son profil. Le contenu du catalogue est administré via l'interface d'administration de Django.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)
![Base de données](https://img.shields.io/badge/base%20de%20données-SQLite-003B57?logo=sqlite&logoColor=white)
![Tests](https://img.shields.io/badge/tests-aucun-6b7280)

---

## Le problème

Les avis qu'on se fait d'un film finissent dans un carnet, une note de téléphone ou un fil de discussion : personne d'autre ne les lit, et l'auteur lui-même ne retrouve pas ce qu'il avait écrit sur un titre vu deux ans plus tôt.

Cette application rassemble les films et les critiques au même endroit, chaque critique restant rattachée à son film et à son auteur.

## Fonctionnalités

- **Catalogue paginé** — dix films par page, chacun avec son synopsis, ses réalisateurs, ses genres, ses pays de production, sa durée et son année de sortie en France.
- **Recherche par titre** — sur une partie du titre, sans tenir compte de la casse (« ali » trouve *Alien*).
- **Critiques par film** — la liste affiche les vingt premiers mots de chaque critique, avec son auteur et sa date ; un lien ouvre le texte complet.
- **Comptes utilisateurs** — inscription avec règles vérifiées à la saisie : nom d'utilisateur de 6 à 50 caractères alphanumériques, mot de passe d'au moins 10 caractères comportant majuscule, minuscule, chiffre et caractère spécial.
- **Espace personnel** — le profil liste les critiques de l'utilisateur connecté et permet de les relire, modifier ou supprimer ; modification et suppression sont refusées à quiconque n'en est pas l'auteur.
- **Administration du catalogue** — films, réalisateurs, genres et pays se saisissent dans l'admin Django, avec autocomplétion sur les relations et édition directe depuis la liste ; une critique peut y être dépubliée sans être supprimée.

## Technologies

| Outil | Rôle |
|---|---|
| [Python 3.12](https://www.python.org/) | Langage |
| [Django 5.2](https://www.djangoproject.com/) | Modèles, vues, formulaires, authentification, administration |
| [django-environ](https://django-environ.readthedocs.io/) | Lecture de la `SECRET_KEY` depuis un fichier `.env` |
| [SQLite](https://www.sqlite.org/) | Base de données locale, sans service à installer |

## Installation

Prérequis : Python 3.12. Aucun service externe, la base est un simple fichier.

```bash
git clone git@github.com:Incapas/movie-review-website.git
cd movie-review-website

python3.12 -m venv env
source env/bin/activate          # Windows : env\Scripts\activate
pip install -r requirements.txt
```

Variable d'environnement, à placer dans `src/website/.env` :

| Variable | Provenance |
|---|---|
| `SECRET_KEY` | Chaîne aléatoire générée localement, propre à l'installation. |

Sans ce fichier, une clé par défaut est utilisée : l'application démarre, mais cette valeur n'a rien de secret et ne doit pas servir au-delà d'un essai.

Préparation de la base, depuis le dossier `src/` :

```bash
cd src
python manage.py migrate
python manage.py createsuperuser
```

## Utilisation

```bash
cd src
python manage.py runserver
```

L'application répond sur `http://127.0.0.1:8000/`. La page d'accueil est le catalogue ; la barre de navigation mène à l'inscription, à la connexion puis au profil.

Sur une base neuve, le catalogue est vide : les films s'ajoutent d'abord depuis `http://127.0.0.1:8000/admin/`, avec le compte créé par `createsuperuser`. `manage.py` se trouve dans `src/` — lancé depuis la racine du dépôt, le serveur ne démarre pas.

`DEBUG` est à `True` et `ALLOWED_HOSTS` est vide : cette configuration est celle d'un développement local, pas d'une mise en ligne.

## Tests

```bash
cd src
python manage.py test
```

Il n'existe aujourd'hui aucun test : les fichiers `tests.py` des trois applications sont les squelettes créés par Django et la commande ne vérifie donc rien. Il n'y a pas non plus de mesure de couverture.

## Structure du projet

```
src/
  manage.py                Point d'entrée des commandes Django
  website/                 Projet : réglages, URLs racines, gabarit et styles communs
    settings.py            Configuration, lecture du .env, langue fr-FR
    urls.py                Aiguillage : / → movies, /film/ → reviews, /utilisateur/ → accounts
  accounts/                Inscription, connexion, déconnexion, profil
    forms.py               Règles de validation du nom d'utilisateur et du mot de passe
  movies/                  Catalogue : Movie, Director, Gender, Country
    views.py               Liste paginée et recherche par titre
  reviews/                 Critiques : lecture, rédaction, modification, suppression
    models.py              Review, rattachée à un film et à son auteur
```

Chaque application embarque ses propres gabarits (`templates/<app>/`) et ses feuilles de style (`static/<app>/`) ; seuls le gabarit de base et les styles partagés vivent dans `website/`. Les dépendances vont des critiques vers les films et les utilisateurs, jamais l'inverse : `movies` ignore `reviews`.

## Contributeurs

### Développeur

Conception, décisions et validation du produit :

- définition du besoin et des règles métier : modélisation des films et de leurs relations, critique rattachée à un film et à un auteur, droit de modification réservé à l'auteur, règles d'inscription ;
- choix d'ergonomie : catalogue comme page d'accueil, recherche par titre, pagination à dix films, profil regroupant ses propres critiques ;
- choix techniques structurants : Django, découpage en applications `accounts` / `movies` / `reviews`, code applicatif isolé dans `src/`, URLs en français, `SECRET_KEY` sortie du dépôt via `django-environ` ;
- écriture du backend : modèles, vues, formulaires, URLs, configuration de l'administration et migrations.

### Assistant IA — Gemini

Réalisation de la couche de présentation sous la direction du développeur :

- structure des gabarits HTML : gabarit de base, navigation, formulaires, listes de films et de critiques ;
- feuilles de style de chaque application et mise en page d'ensemble ;
- mise en forme des formulaires d'inscription, de connexion et de rédaction de critique.

Chaque modification a été relue et validée par le développeur avant intégration.

## Licence

GNU General Public License, version 3, 29 juin 2007.