
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

# class ClasseEnseignantSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Classe

#         fields = [
#             'id_classe',
#             'nom',
#             'enseignant',
#             'date_creation'
#         ]




class ClasseEnseignantSerializer(serializers.ModelSerializer):
    # Champs calculés
    nb_eleves = serializers.SerializerMethodField()
    nb_matieres = serializers.SerializerMethodField()

    class Meta:
        model = Classe
        fields = [
            'id_classe',
            'nom',
            'enseignant',
            'nb_eleves',
            'nb_matieres',
        ]

    def get_nb_eleves(self, obj):
        return obj.eleves.count()

    def get_nb_matieres(self, obj):
        return obj.matieres.count()


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

# class NoteSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Note

#         fields = [
#             'id_note',
#             'eleve',
#             'enseignant',
#             'type_evaluation',
#             'matiere',
#             'sequence',
#             'moyenne'
#         ]

#         read_only_fields = [
#             'id_note',
#             'enseignant',
#             'eleve'
#         ]

#     def validate_moyenne(self, value):

#         if value < 0 or value > 20:
#             raise serializers.ValidationError(
#                 "La moyenne doit être comprise entre 0 et 20."
#             )

#         return value




class NoteSerializer(serializers.ModelSerializer):
    # Champs calculés
    eleve_nom = serializers.SerializerMethodField()
    matiere_nom = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = [
            'id_note',
            'eleve',
            'eleve_nom',
            'enseignant',
            'type_evaluation',
            'matiere',
            'matiere_nom',
            'sequence',
            'moyenne',
        ]
        read_only_fields = [
            'id_note',
            'enseignant',
            'eleve',
            'eleve_nom',
            'matiere_nom',
        ]

    def get_eleve_nom(self, obj):
        return obj.eleve.nom if obj.eleve else None

    def get_matiere_nom(self, obj):
        return obj.matiere.nom if obj.matiere else None

    def validate_moyenne(self, value):
        if value < 0 or value > 20:
            raise serializers.ValidationError(
                "La moyenne doit être comprise entre 0 et 20."
            )
        return value


# ============================================================
# ABSENCE
# ============================================================

# class AbsenceSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Absence

#         fields = [
#             'id_absence',
#             'eleve',
#             'enseignant',
#             'date_absence',
#             'matiere'
#         ]

#         read_only_fields = [
#             'id_absence',
#             'enseignant',
#             'eleve'
#         ]


class AbsenceSerializer(serializers.ModelSerializer):
    eleve_nom = serializers.SerializerMethodField()
    matiere_nom = serializers.SerializerMethodField()

    class Meta:
        model = Absence
        fields = [
            'id_absence',
            'eleve',
            'eleve_nom',
            'enseignant',
            'date_absence',
            'matiere',
            'matiere_nom',
            'statut',
            'motif',
        ]
        read_only_fields = [
            'id_absence',
            'enseignant',
            'eleve',
            'eleve_nom',
            'matiere_nom',
        ]

    def get_eleve_nom(self, obj):
        return obj.eleve.nom if obj.eleve else None

    def get_matiere_nom(self, obj):
        return obj.matiere.nom if obj.matiere else None

# ============================================================
# REMARQUE
# ============================================================

# class RemarqueSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Remarque

#         fields = [
#             'id_remarque',
#             'eleve',
#             'enseignant',
#             'type',
#             'contenu',
#             'date_remarque'
#         ]

#         read_only_fields = [
#             'id_remarque',
#             'enseignant',
#             'eleve',
#             'date_remarque'
#         ]


class RemarqueSerializer(serializers.ModelSerializer):
    eleve_nom = serializers.SerializerMethodField()

    class Meta:
        model = Remarque
        fields = [
            'id_remarque',
            'eleve',
            'eleve_nom',
            'enseignant',
            'type',
            'contenu',
            'date_remarque',
        ]
        read_only_fields = [
            'id_remarque',
            'enseignant',
            'eleve',
            'eleve_nom',
            'date_remarque',
        ]

    def get_eleve_nom(self, obj):
        return obj.eleve.nom if obj.eleve else None

# ============================================================
# SANCTION
# ============================================================

# class SanctionSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Sanction

#         fields = [
#             'id_sanction',
#             'eleve',
#             'enseignant',
#             'type_sanction',
#             'motif',
#             'date_sanction'
#         ]

#         read_only_fields = [
#             'id_sanction',
#             'enseignant',
#             'eleve',
#             'date_sanction'
#         ]



class SanctionSerializer(serializers.ModelSerializer):
    eleve_nom = serializers.SerializerMethodField()

    class Meta:
        model = Sanction
        fields = [
            'id_sanction',
            'eleve',
            'eleve_nom',
            'enseignant',
            'type_sanction',
            'motif',
            'date_sanction',
        ]
        read_only_fields = [
            'id_sanction',
            'enseignant',
            'eleve',
            'eleve_nom',
            'date_sanction',
        ]

    def get_eleve_nom(self, obj):
        return obj.eleve.nom if obj.eleve else None

# ============================================================
# BULLETIN
# ============================================================

class BulletinSerializer(serializers.ModelSerializer):
    eleve_nom = serializers.SerializerMethodField()
    fichier_url = serializers.SerializerMethodField()
    trimestre_display = serializers.CharField(source='get_trimestre_display', read_only=True)
    sequence_display = serializers.CharField(source='get_sequence_display', read_only=True)

    class Meta:
        model = Bulletin
        fields = [
            'id_bulletin',
            'eleve',
            'eleve_nom',
            'enseignant',
            'trimestre',
            'trimestre_display',
            'sequence',
            'sequence_display',
            'annee_scolaire',
            'fichier',
            'fichier_url',
            'date_publication',
        ]
        read_only_fields = [
            'id_bulletin',
            'enseignant',
            'eleve',
            'eleve_nom',
            'fichier_url',
            'date_publication',
            'trimestre_display',
            'sequence_display',
        ]

    def get_eleve_nom(self, obj):
        return obj.eleve.nom if obj.eleve else None

    def get_fichier_url(self, obj):
        request = self.context.get('request')
        if obj.fichier and request:
            return request.build_absolute_uri(obj.fichier.url)
        return None