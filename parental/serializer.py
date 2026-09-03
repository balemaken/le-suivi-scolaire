from rest_framework import serializers

from user.models import Utilisateur

from administration.models import (
    Eleve,
    Classe,
    Matiere,
    LiaisonParentEleve
)

from enseignement.models import (
    Note,
    Absence,
    Remarque,
    Sanction,
    Bulletin
)


# ============================================================
# ELEVE
# ============================================================

class EleveParentSerializer(serializers.ModelSerializer):

    classe_nom = serializers.CharField(
        source='classe.nom',
        read_only=True
    )

    id_classe = serializers.IntegerField(
        source='classe.id_classe',
        read_only=True
    )

    class Meta:
        model = Eleve

        fields = [
            'id_eleve',
            'nom',
            'sexe',
            'id_classe',
            'classe_nom'
        ]


# ============================================================
# PARENT
# ============================================================

class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur

        fields = [
            'id_utilisateur',
            'nom',
            'prenom',
            'role',
            'sexe',
            'telephone',
            'email'
        ]

        read_only_fields = fields


# ============================================================
# LIAISON PARENT - ELEVE
# ============================================================

class LiaisonParentSerializer(serializers.ModelSerializer):

    eleve = EleveParentSerializer(
        read_only=True
    )

    class Meta:
        model = LiaisonParentEleve

        fields = [
            'id_liaison',
            'eleve',
            'date_liaison'
        ]

        read_only_fields = fields


# ============================================================
# NOTE
# ============================================================

class NoteParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note

        fields = [
            'id_note',
            'type_evaluation',
            'matiere',
            'sequence',
            'moyenne'
        ]

        read_only_fields = fields


# ============================================================
# ABSENCE
# ============================================================

class AbsenceParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Absence

        fields = [
            'id_absence',
            'date_absence',
            'matiere'
        ]

        read_only_fields = fields


# ============================================================
# REMARQUE
# ============================================================

class RemarqueParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Remarque

        fields = [
            'id_remarque',
            'type',
            'contenu',
            'date'
        ]

        read_only_fields = fields


# ============================================================
# SANCTION
# ============================================================

class SanctionParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sanction

        fields = [
            'id_sanction',
            'type_sanction',
            'motif',
            'date'
        ]

        read_only_fields = fields


# ============================================================
# BULLETIN
# ============================================================

class BulletinParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bulletin

        fields = [
            'id_bulletin',
            'fichier',
            'date'
        ]

        read_only_fields = fields