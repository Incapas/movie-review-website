# 🎬 Critiques de film (Django)

## Description du Projet

Ce projet est une application web de critiques de films développée avec le framework **Django** (Python). Conçue pour l'apprentissage et l'initiation au développement web *full-stack*, l'application permet aux utilisateurs de **consulter les critiques** soumises par les autres membres et, après inscription, d'**écrire et de gérer leurs propres critiques** de films.

L'application est légère, axée sur les opérations **CRUD** (Create, Read, Update, Delete) de base pour les critiques, les films et les comptes utilisateurs.

### Architecture d'Applications

Le projet est divisé en plusieurs applications (apps) pour une structure modulaire typique de Django :

* **`website`** : Configuration principale du projet et pages statiques (accueil, etc.).
* **`accounts`** : Gestion des utilisateurs (inscription, connexion/déconnexion).
* **`movies`** : Modèles et vues pour la gestion des données de base sur les films.
* **`reviews`** : Logique et modèles pour la soumission, l'affichage et la gestion des critiques.

---

## 👥 Contributions au Projet

### 👩 Développeur Initial

Contribution résidant dans la **conception de l'architecture backend** (modèles, vues, URLs), la **sécurité** et la **logique d'interaction** de l'application.

| Catégorie | Description de la contribution |
| :--- | :--- |
| **Architecture Django** | Conception des modèles (`models.py`) pour les utilisateurs, les films et les critiques. |
| **Logique Fonctionnelle** | Développement de toutes les **Vues (Views)** et des **URLs (URLConf)** pour la navigation et les opérations CRUD. |
| **Base de Données** | Configuration de la base de données (SQLite par défaut) et gestion des migrations. |
| **Sécurité/Comptes** | Implémentation du système d'authentification et d'autorisation Django (app `accounts`). |

### 🧑 Assistant IA Gemini

Contribution entièrement axée sur la **couche de présentation** pour offrir une interface utilisateur agréable et réactive sans détourner l'attention du développeur de la logique backend.

| Catégorie | Description de la Contribution |
| :--- | :--- |
| **Structure HTML** | Création de la structure et du balisage des templates HTML de base (`base.html`, formulaires, affichage des listes). |
| **Stylisation (CSS)** | Réalisation de l'intégralité du **CSS** (feuilles de style) pour assurer la mise en page, le design et la responsivité. |
| **Intégration Front-end** | Mise en forme des formulaires d'authentification et de soumission de critiques. |

---

## 🛠️ Prérequis

Ce projet n'est pas destiné à être déployé en production. L'exécution se fait uniquement en local.

### Prérequis

Assurez-vous d'avoir **Python** installé sur votre système.

1.  **Python 3.x**
2.  Les dépendances nécessaires (Django, etc.).

```bash
pip install -r requirements.txt
````

-----

## 🚀 Démarrage

### 💻 Exécution locale

1.  **Clonez le dépôt :**

    ```bash
    git clone [URL_DEPOT]
    cd [NOM_DU_DEPOT]
    ```

2.  **Installez les dépendances :**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Appliquez les migrations :**
    Créez la structure de la base de données SQLite.

    ```bash
    python manage.py migrate
    ```

4.  **Lancez le serveur de développement :**
    Le serveur sera accessible à `http://127.0.0.1:8000/`.

    ```bash
    python manage.py runserver
    ```

-----

## 📝 Guide d'Utilisation

1.  **Accéder à l'application** : Ouvrez votre navigateur et naviguez vers l'adresse indiquée par le serveur (`http://127.0.0.1:8000/`).
2.  **Consulter** : La page d'accueil affiche les films ou les dernières critiques. Vous pouvez parcourir le contenu sans être connecté.
3.  **S'inscrire** : Pour écrire une critique, cliquez sur l'option d'inscription (ou `Sign Up`) pour créer votre compte utilisateur (via l'app `accounts`).
4.  **Écrire une Critique** : Une fois connecté, naviguez vers un film et utilisez le formulaire pour soumettre votre évaluation (via l'app `reviews`).
5.  **Gérer le Contenu** : Les utilisateurs peuvent modifier ou supprimer uniquement les critiques qu'ils ont écrites.