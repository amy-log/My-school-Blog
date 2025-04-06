from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')  # Colonnes affichées
    search_fields = ('titre', 'contenu')  # Barre de recherche
    list_filter = ('date_publication', 'auteur')  # Filtres sur le côté

