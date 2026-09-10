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

# class NoteParentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Note

#         fields = [
#             'id_note',
#             'type_evaluation',
#             'matiere',
#             'sequence',
#             'moyenne'
#         ]

#         read_only_fields = fields


class NoteParentSerializer(serializers.ModelSerializer):
    matiere_nom = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = [
            'id_note',
            'type_evaluation',
            'matiere',
            'matiere_nom',
            'sequence',
            'moyenne',
        ]
        read_only_fields = fields

    def get_matiere_nom(self, obj):
        return obj.matiere.nom if obj.matiere else '—'


# ============================================================
# ABSENCE
# ============================================================

# class AbsenceParentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Absence

#         fields = [
#             'id_absence',
#             'date_absence',
#             'matiere'
#         ]

#         read_only_fields = fields

class AbsenceParentSerializer(serializers.ModelSerializer):
    matiere_nom = serializers.SerializerMethodField()

    class Meta:
        model = Absence
        fields = [
            'id_absence',
            'date_absence',
            'matiere',
            'matiere_nom',
        ]
        read_only_fields = fields

    def get_matiere_nom(self, obj):
        return obj.matiere.nom if obj.matiere else '—'
# ============================================================
# REMARQUE
# ============================================================

# class RemarqueParentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Remarque

#         fields = [
#             'id_remarque',
#             'type',
#             'contenu',
#             'date'
#         ]

#         read_only_fields = fields

class RemarqueParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remarque
        fields = [
            'id_remarque',
            'type',
            'contenu',
            'date_remarque',
        ]
        read_only_fields = fields
# ============================================================
# SANCTION
# ============================================================

# class SanctionParentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Sanction

#         fields = [
#             'id_sanction',
#             'type_sanction',
#             'motif',
#             'date'
#         ]

#         read_only_fields = fields

class SanctionParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanction
        fields = [
            'id_sanction',
            'type_sanction',
            'motif',
            'date_sanction',
        ]
        read_only_fields = fields
# ============================================================
# BULLETIN
# ============================================================

# class BulletinParentSerializer(serializers.ModelSerializer):
#     fichier_url = serializers.SerializerMethodField()

#     class Meta:
#         model = Bulletin
#         fields = [
#             'id_bulletin',
#             'fichier',
#             'fichier_url',
#             'date_publication',
#         ]
#         read_only_fields = fields

#     def get_fichier_url(self, obj):
#         request = self.context.get('request')
#         if obj.fichier and request:
#             return request.build_absolute_uri(obj.fichier.url)
#         return None




class BulletinParentSerializer(serializers.ModelSerializer):
    fichier_url = serializers.SerializerMethodField()
    trimestre_display = serializers.CharField(source='get_trimestre_display', read_only=True)
    sequence_display = serializers.CharField(source='get_sequence_display', read_only=True)

    class Meta:
        model = Bulletin
        fields = [
            'id_bulletin',
            'trimestre',
            'trimestre_display',
            'sequence',
            'sequence_display',
            'annee_scolaire',
            'fichier',
            'fichier_url',
            'date_publication',
        ]
        read_only_fields = fields

    def get_fichier_url(self, obj):
        request = self.context.get('request')
        if obj.fichier and request:
            return request.build_absolute_uri(obj.fichier.url)
        return None