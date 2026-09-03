from rest_framework import serializers
from .models import Classe, Eleve, Matiere
from user.models import Utilisateur


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ['id_classe', 'nom', 'enseignant']

    def validate_enseignant(self, value):
        if value is not None and value.role != 'enseignant':
            raise serializers.ValidationError(
                "L'utilisateur sélectionné n'est pas un enseignant."
            )
        return value


class EleveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleve
        fields = ['id_eleve', 'nom', 'sexe', 'classe']


class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = ['id_matiere', 'nom', 'classe', 'enseignant']

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


class ParentSerializer(serializers.ModelSerializer):

    enfant = EnfantSerializer(
        many=True,
        read_only=True
    )

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
            'enfant'
        ]

        read_only_fields = [
            'id_utilisateur',
            'role',
            'enfant'
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