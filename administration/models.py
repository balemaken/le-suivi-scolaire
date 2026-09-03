from django.db import models

# Create your models here.
from django.db import models
from user.models import Utilisateur


class Classe(models.Model):

    id_classe = models.AutoField(primary_key=True)

    nom = models.CharField(
        max_length=100,
        unique=True
    )

    # Enseignant responsable de la classe
    enseignant = models.ForeignKey(
        Utilisateur,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='classes_responsables',
        limit_choices_to={'role': 'enseignant'}
    )

    def __str__(self):
        return self.nom


class Eleve(models.Model):

    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    id_eleve = models.AutoField(primary_key=True)

    nom = models.CharField(
        max_length=100
    )

    sexe = models.CharField(
        max_length=1,
        choices=SEXE_CHOICES
    )

    # Un élève appartient à une seule classe
    classe = models.ForeignKey(
        Classe,
        on_delete=models.CASCADE,
        related_name='eleves'
    )

    def __str__(self):
        return self.nom


class Matiere(models.Model):

    id_matiere = models.AutoField(primary_key=True)

    nom = models.CharField(
        max_length=100
    )

    # La matière appartient à une classe
    classe = models.ForeignKey(
        Classe,
        on_delete=models.CASCADE,
        related_name='matieres'
    )

    # Enseignant affecté à la matière
    enseignant = models.ForeignKey(
        Utilisateur,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='matieres_enseignees',
        limit_choices_to={'role': 'enseignant'}
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom', 'classe'],
                name='unique_matiere_par_classe'
            )
        ]

    def __str__(self):
        return self.nom















class LiaisonParentEleve(models.Model):

    id_liaison = models.AutoField(
        primary_key=True
    )

    parent = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='liaisons_eleves',
        limit_choices_to={'role': 'parent'}
    )

    eleve = models.ForeignKey(
        Eleve,
        on_delete=models.CASCADE,
        related_name='liaisons_parents'
    )

    date_liaison = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent', 'eleve'],
                name='unique_parent_eleve'
            )
        ]

    def __str__(self):
        return f"{self.parent} - {self.eleve}"

