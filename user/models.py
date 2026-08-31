from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Enfant(models.Model):

    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    id_enfant = models.AutoField(primary_key=True)

    nom = models.CharField(max_length=100)

    sexe = models.CharField(
        max_length=1,
        choices=SEXE_CHOICES
    )

    classe = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Utilisateur(AbstractUser):

    ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('enseignant', 'Enseignant'),
        ('admin', 'Administrateur'),
    ]

    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    username = None

    id_utilisateur = models.AutoField(
        primary_key=True
    )

    nom = models.CharField(
        max_length=100
    )

    prenom = models.CharField(
        max_length=100,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    sexe = models.CharField(
        max_length=1,
        choices=SEXE_CHOICES,
        blank=True
    )

    telephone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        unique=True
    )

    matricule = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )

    enfant = models.ManyToManyField(
        Enfant,
        blank=True,
        related_name='parents'
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nom']

    def __str__(self):
        return f"{self.nom} {self.prenom}"