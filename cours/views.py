from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Enseignant, Cours
from .forms import EnseignantForm, CoursForm  


def accueil(request):
    return render(request, 'cours/accueil.html')


def connexion_utilisateur(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('liste_cours')
        else:
            message = "Nom d'utilisateur ou mot de passe incorrect."
    return render(request, 'cours/connexion.html', {'message': message})


def deconnexion_utilisateur(request):
    logout(request)
    return redirect('connexion')


@login_required
def accueil_enseignant(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'cours/Enseignant/accueil_enseignant.html', {'enseignants': enseignants})


@login_required
def ajouter_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil_enseignant')
    else:
        form = EnseignantForm()
    return render(request, 'cours/Enseignant/ajouter_enseignant.html', {'form': form})


@login_required
def modifier_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignant, id=pk)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('accueil_enseignant')
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'cours/Enseignant/modifier_enseignant.html', {'form': form})


@login_required
def supprimer_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignant, id=pk)
    enseignant.delete()
    return redirect('accueil_enseignant')


@login_required
def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/liste_cours.html', {'cours': cours})


@login_required
def ajouter_cours(request):
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_cours')
    else:
        form = CoursForm()
    return render(request, 'cours/ajouter_cours.html', {'form': form})


@login_required
def modifier_cours(request, id):
    un_cours = get_object_or_404(Cours, id=id)
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=un_cours)
        if form.is_valid():
            form.save()
            return redirect('liste_cours')
    else:
        form = CoursForm(instance=un_cours)
    return render(request, 'cours/modifier_cours.html', {'form': form})


@login_required
def supprimer_cours(request, id):
    un_cours = get_object_or_404(Cours, id=id)
    un_cours.delete()
    return redirect('liste_cours')