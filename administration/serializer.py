from rest_framework import serializers
from .models import Classe, Eleve, Matiere
from user.models import Utilisateur


# class ClasseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Classe
#         fields = ['id_classe', 'nom', 'enseignant']

#     def validate_enseignant(self, value):
#         if value is not None and value.role != 'enseignant':
#             raise serializers.ValidationError(
#                 "L'utilisateur sélectionné n'est pas un enseignant."
#             )
#         return value



class ClasseSerializer(serializers.ModelSerializer):
    # Champs calculés
    nb_eleves = serializers.SerializerMethodField()
    nb_matieres = serializers.SerializerMethodField()
    enseignant_nom = serializers.SerializerMethodField()

    class Meta:
        model = Classe
        fields = [
            'id_classe',
            'nom',
            'enseignant',
            'enseignant_nom',
            'nb_eleves',
            'nb_matieres',
        ]

    def get_nb_eleves(self, obj):
        return obj.eleves.count()

    def get_nb_matieres(self, obj):
        return obj.matieres.count()

    def get_enseignant_nom(self, obj):
        if obj.enseignant:
            return f"{obj.enseignant.prenom} {obj.enseignant.nom}".strip()
        return None

    def validate_enseignant(self, value):
        if value is not None and value.role != 'enseignant':
            raise serializers.ValidationError(
                "L'utilisateur sélectionné n'est pas un enseignant."
            )
        return value








# class EleveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Eleve
#         fields = ['id_eleve', 'nom', 'sexe', 'classe']

class EleveSerializer(serializers.ModelSerializer):
    # Champ calculé pour afficher le nom de la classe
    classe_nom = serializers.SerializerMethodField()

    class Meta:
        model = Eleve
        fields = [
            'id_eleve',
            'nom',
            'sexe',
            'classe',
            'classe_nom',
        ]

    def get_classe_nom(self, obj):
        return obj.classe.nom if obj.classe else None






# class MatiereSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Matiere
#         fields = ['id_matiere', 'nom', 'classe', 'enseignant']

#     def validate_enseignant(self, value):
#         if value is not None and value.role != 'enseignant':
#             raise serializers.ValidationError(
#                 "L'utilisateur sélectionné n'est pas un enseignant."
#             )
#         return value






class MatiereSerializer(serializers.ModelSerializer):
    # Champs calculés
    classe_nom = serializers.SerializerMethodField()
    enseignant_nom = serializers.SerializerMethodField()

    class Meta:
        model = Matiere
        fields = [
            'id_matiere',
            'nom',
            'classe',
            'classe_nom',
            'enseignant',
            'enseignant_nom',
        ]

    def get_classe_nom(self, obj):
        return obj.classe.nom if obj.classe else None

    def get_enseignant_nom(self, obj):
        if obj.enseignant:
            return f"{obj.enseignant.prenom} {obj.enseignant.nom}".strip()
        return None

    def validate_enseignant(self, value):
        if value is not None and value.role != 'enseignant':
            raise serializers.ValidationError(
                "L'utilisateur sélectionné n'est pas un enseignant."
            )
        return value










from rest_framework import serializers
from .models import Classe, Eleve, Matiere, LiaisonParentEleve
from user.models import Utilisateur, Enfant



class EnfantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfant
        fields = [
            'id_enfant',
            'nom',
            'sexe',
            'classe'
        ]


# class ParentSerializer(serializers.ModelSerializer):

#     enfant = EnfantSerializer(
#         many=True,
#         read_only=True
#     )

#     class Meta:
#         model = Utilisateur
#         fields = [
#             'id_utilisateur',
#             'nom',
#             'prenom',
#             'role',
#             'sexe',
#             'telephone',
#             'email',
#             'matricule',
#             'enfant'
#         ]

#         read_only_fields = [
#             'id_utilisateur',
#             'role',
#             'enfant'
#         ]




class ParentSerializer(serializers.ModelSerializer):
    # Enfants auto-déclarés (table Enfant)
    enfant = EnfantSerializer(many=True, read_only=True)

    # Élèves réellement liés via LiaisonParentEleve
    eleves_lies = serializers.SerializerMethodField()

    class Meta:
        model = Utilisateur
        fields = [
            'id_utilisateur',
            'nom',
            'prenom',
            'role',
            'sexe',
            'telephone',
            'email',
            'matricule',
            'is_active',
            'enfant',
            'eleves_lies',
        ]
        read_only_fields = [
            'id_utilisateur',
            'role',
            'enfant',
            'eleves_lies',
        ]

    def get_eleves_lies(self, obj):
        """Récupère les élèves liés via LiaisonParentEleve"""
        liaisons = LiaisonParentEleve.objects.filter(
            parent=obj
        ).select_related('eleve', 'eleve__classe')

        return [
            {
                'id_eleve': l.eleve.id_eleve,
                'nom': l.eleve.nom,
                'sexe': l.eleve.sexe,
                'classe': l.eleve.classe.nom if l.eleve.classe else '',
                'id_classe': l.eleve.classe.id_classe if l.eleve.classe else None,
            }
            for l in liaisons
        ]








class LiaisonParentEleveSerializer(serializers.ModelSerializer):

    parent = ParentSerializer(
        read_only=True
    )

    class Meta:
        model = LiaisonParentEleve
        fields = [
            'id_liaison',
            'parent',
            'eleve',
            'date_liaison'
        ]

        read_only_fields = [
            'id_liaison',
            'date_liaison'
        ]


class CreerLiaisonSerializer(serializers.Serializer):

    id_eleve = serializers.IntegerField()