
from rest_framework import serializers

from .models import (
    Note,
    Absence,
    Remarque,
    Sanction,
    Bulletin
)

from administration.models import (
    Classe,
    Eleve,
    Matiere
)


# ============================================================
# CLASSE
# ============================================================

class ClasseEnseignantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classe

        fields = [
            'id_classe',
            'nom',
            'enseignant',
            'date_creation'
        ]


# ============================================================
# ELEVE
# ============================================================

class EleveEnseignantSerializer(serializers.ModelSerializer):

    classe_nom = serializers.CharField(
        source='classe.nom',
        read_only=True
    )

    class Meta:
        model = Eleve

        fields = [
            'id_eleve',
            'nom',
            'sexe',
            'classe',
            'classe_nom'
        ]


# ============================================================
# MATIERE
# ============================================================

class MatiereEnseignantSerializer(serializers.ModelSerializer):

    classe_nom = serializers.CharField(
        source='classe.nom',
        read_only=True
    )

    class Meta:
        model = Matiere

        fields = [
            'id_matiere',
            'nom',
            'classe',
            'classe_nom',
            'enseignant'
        ]


# ============================================================
# NOTE
# ============================================================

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note

        fields = [
            'id_note',
            'eleve',
            'enseignant',
            'type_evaluation',
            'matiere',
            'sequence',
            'moyenne'
        ]

        read_only_fields = [
            'id_note',
            'enseignant',
            'eleve'
        ]

    def validate_moyenne(self, value):

        if value < 0 or value > 20:
            raise serializers.ValidationError(
                "La moyenne doit être comprise entre 0 et 20."
            )

        return value


# ============================================================
# ABSENCE
# ============================================================

class AbsenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Absence

        fields = [
            'id_absence',
            'eleve',
            'enseignant',
            'date_absence',
            'matiere'
        ]

        read_only_fields = [
            'id_absence',
            'enseignant',
            'eleve'
        ]


# ============================================================
# REMARQUE
# ============================================================

class RemarqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Remarque

        fields = [
            'id_remarque',
            'eleve',
            'enseignant',
            'type',
            'contenu',
            'date_remarque'
        ]

        read_only_fields = [
            'id_remarque',
            'enseignant',
            'eleve',
            'date_remarque'
        ]


# ============================================================
# SANCTION
# ============================================================

class SanctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sanction

        fields = [
            'id_sanction',
            'eleve',
            'enseignant',
            'type_sanction',
            'motif',
            'date_sanction'
        ]

        read_only_fields = [
            'id_sanction',
            'enseignant',
            'eleve',
            'date_sanction'
        ]


# ============================================================
# BULLETIN
# ============================================================

class BulletinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bulletin

        fields = [
            'id_bulletin',
            'eleve',
            'enseignant',
            'fichier',
            'date_publication'
        ]

        read_only_fields = [
            'id_bulletin',
            'enseignant',
            'eleve',
            'date_publication'
        ]
