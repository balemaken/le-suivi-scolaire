from django.db import models

# Create your models here.

from django.db import models

from user.models import Utilisateur
from administration.models import Eleve, Matiere


# ============================================================
# NOTE
# ============================================================

class Note(models.Model):

    TYPE_EVALUATION_CHOICES = [
        ('controle_continu', 'Contrôle continu'),
        ('devoir_harmonise', 'Devoir harmonisé'),
    ]

    SEQUENCE_CHOICES = [
        (1, 'Séquence 1'),
        (2, 'Séquence 2'),
        (3, 'Séquence 3'),
        (4, 'Séquence 4'),
        (5, 'Séquence 5'),
        (6, 'Séquence 6'),
    ]

    id_note = models.AutoField(primary_key=True)

    eleve = models.ForeignKey(
        Eleve,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    enseignant = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='notes_saisies',
        limit_choices_to={'role': 'enseignant'}
    )

    type_evaluation = models.CharField(
        max_length=30,
        choices=TYPE_EVALUATION_CHOICES
    )

    matiere = models.ForeignKey(
        Matiere,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    sequence = models.PositiveSmallIntegerField(
        choices=SEQUENCE_CHOICES
    )

    moyenne = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.eleve.nom} - {self.matiere.nom}"


# ============================================================
# ABSENCE
# ============================================================

# class Absence(models.Model):

#     id_absence = models.AutoField(primary_key=True)

#     eleve = models.ForeignKey(
#         Eleve,
#         on_delete=models.CASCADE,
#         related_name='absences'
#     )

#     enseignant = models.ForeignKey(
#         Utilisateur,
#         on_delete=models.CASCADE,
#         related_name='absences_saisies',
#         limit_choices_to={'role': 'enseignant'}
#     )

#     date_absence = models.DateField()

#     matiere = models.ForeignKey(
#         Matiere,
#         on_delete=models.CASCADE,
#         related_name='absences'
#     )

#     def __str__(self):
#         return f"Absence - {self.eleve.nom}"



class Absence(models.Model):

    STATUT_CHOICES = [
        ('justifiee', 'Justifiée'),
        ('non-justifiee', 'Non justifiée'),
        ('autre', 'Autre'),
    ]

    id_absence = models.AutoField(primary_key=True)

    eleve = models.ForeignKey(
        Eleve,
        on_delete=models.CASCADE,
        related_name='absences'
    )

    enseignant = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='absences_saisies',
        limit_choices_to={'role': 'enseignant'}
    )

    date_absence = models.DateField()

    matiere = models.ForeignKey(
        Matiere,
        on_delete=models.CASCADE,
        related_name='absences'
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='non-justifiee'
    )

    motif = models.TextField(
        blank=True,
        default=''
    )

    def __str__(self):
        return f"Absence - {self.eleve.nom}"


# ============================================================
# REMARQUE
# ============================================================

class Remarque(models.Model):

    TYPE_REMARQUE_CHOICES = [
        ('positif', 'Positif'),
        ('negatif', 'Négatif'),
        ('autre', 'Autre'),
    ]

    id_remarque = models.AutoField(primary_key=True)

    eleve = models.ForeignKey(
        Eleve,
        on_delete=models.CASCADE,
        related_name='remarques'
    )

    enseignant = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='remarques_saisies',
        limit_choices_to={'role': 'enseignant'}
    )

    type = models.CharField(
        max_length=20,
        choices=TYPE_REMARQUE_CHOICES
    )

    contenu = models.TextField()

    # Date de la remarque
    date_remarque = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Remarque - {self.eleve.nom}"


# ============================================================
# SANCTION
# ============================================================

class Sanction(models.Model):

    TYPE_SANCTION_CHOICES = [
        ('avertissement', 'Avertissement'),
        ('blame', 'Blâme'),
        ('retenue', 'Retenue'),
        ('exclusion', 'Exclusion'),
        ('autre', 'Autre'),
    ]

    id_sanction = models.AutoField(primary_key=True)

    eleve = models.ForeignKey(
        Eleve,
        on_delete=models.CASCADE,
        related_name='sanctions'
    )

    enseignant = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='sanctions_saisies',
        limit_choices_to={'role': 'enseignant'}
    )

    type_sanction = models.CharField(
        max_length=30,
        choices=TYPE_SANCTION_CHOICES
    )

    motif = models.TextField()

    # Date de la sanction
    date_sanction = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Sanction - {self.eleve.nom}"


# ============================================================
# BULLETIN
# ============================================================

class Bulletin(models.Model):

    TRIMESTRE_CHOICES = [
        ('Trimestre 1', 'Trimestre 1'),
        ('Trimestre 2', 'Trimestre 2'),
        ('Trimestre 3', 'Trimestre 3'),
    ]

    SEQUENCE_CHOICES = [
        (1, 'Séquence 1'),
        (2, 'Séquence 2'),
        (3, 'Séquence 3'),
        (4, 'Séquence 4'),
        (5, 'Séquence 5'),
        (6, 'Séquence 6'),
    ]

    id_bulletin = models.AutoField(primary_key=True)

    eleve = models.ForeignKey(
        Eleve,
        on_delete=models.CASCADE,
        related_name='bulletins'
    )

    enseignant = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='bulletins_saisis',
        limit_choices_to={'role': 'enseignant'}
    )

    trimestre = models.CharField(
        max_length=20,
        choices=TRIMESTRE_CHOICES,
        default='Trimestre 1'
    )

    sequence = models.PositiveSmallIntegerField(
        choices=SEQUENCE_CHOICES,
        default=1
    )

    annee_scolaire = models.CharField(
        max_length=20,
        blank=True,
        default=''
    )

    fichier = models.FileField(
        upload_to='bulletins/'
    )

    date_publication = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Bulletin - {self.eleve.nom} ({self.trimestre} - S{self.sequence})"
