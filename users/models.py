from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (
        ("PARENT", "Parent"),
        ("ENSEIGNANT", "Enseignant"),
        ("ADMIN", "Administrateur"),
    )


    PARENT_TYPE = (
        ("PERE", "Père"),
        ("MERE", "Mère"),
        ("TUTEUR", "Tuteur"),
    )


    email = models.EmailField(
        unique=True
    )


    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )


    telephone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )


    ville = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )


    type_parent = models.CharField(
        max_length=20,
        choices=PARENT_TYPE,
        null=True,
        blank=True
    )


    matricule = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )


    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []


    def __str__(self):

        return self.email





class Enfant(models.Model):

    SEXE = (
        ("MASCULIN","Masculin"),
        ("FEMININ","Feminin"),
    )


    parent = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enfants"
    )


    nom = models.CharField(
        max_length=100
    )


    classe = models.CharField(
        max_length=50
    )


    sexe = models.CharField(
        max_length=10,
        choices=SEXE
    )


    def __str__(self):

        return self.nom