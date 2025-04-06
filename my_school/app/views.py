from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article

# Liste des articles
class ArticleListView(ListView):
    model = Article
    template_name = 'app/article_list.html'
    context_object_name = 'articles'  # Nom de la variable dans le template

# Détail d’un article
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'app/article_detail.html'
    context_object_name = 'article'

# Création d’un nouvel article
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'app/article_form.html'
    fields = ['titre', 'contenu', 'auteur', 'image']
    success_url = reverse_lazy('article_list')

# Modification d’un article
class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'app/article_form.html'
    fields = ['titre', 'contenu', 'image']
    success_url = reverse_lazy('article_list')

# Suppression d’un article
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'app/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')

