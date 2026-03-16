from django.db import models

class Enseignant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.nom 

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    credit = models.IntegerField(default=3)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titre