from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.accueil, name='accueil'),
    
    path('connexion/', views.connexion_utilisateur, name='connexion'),
    path('deconnexion/', views.deconnexion_utilisateur, name='deconnexion'),
    
    path('cours/', views.liste_cours, name='liste_cours'),
    path('cours/ajouter/', views.ajouter_cours, name='ajouter_cours'),
    path('cours/modifier/<int:id>/', views.modifier_cours, name='modifier_cours'),
    path('cours/supprimer/<int:id>/', views.supprimer_cours, name='supprimer_cours'),
    
    path('enseignants/', views.accueil_enseignant, name='accueil_enseignant'),
    path('enseignants/ajouter/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('enseignants/modifier/<int:pk>/', views.modifier_enseignant, name='modifier_enseignant'),
    path('enseignants/supprimer/<int:pk>/', views.supprimer_enseignant, name='supprimer_enseignant'),
]