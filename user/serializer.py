from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Enfant


Utilisateur = get_user_model()


class EnfantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enfant
        fields = [
            'id_enfant',
            'nom',
            'sexe',
            'classe'
        ]
        read_only_fields = ['id_enfant']


class InscriptionSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=6
    )

    enfants = EnfantSerializer(
        many=True,
        required=False
    )

    class Meta:
        model = Utilisateur

        fields = [
            'id_utilisateur',
            'nom',
            'prenom',
            'email',
            'telephone',
            'sexe',
            'matricule',
            'password',
            'enfants',
            'role',
        ]

        read_only_fields = [
            'id_utilisateur',
            'role'
        ]

    @transaction.atomic
    def create(self, validated_data):

        enfants_data = validated_data.pop(
            'enfants',
            []
        )

        password = validated_data.pop(
            'password'
        )

        matricule = validated_data.get(
            'matricule'
        )

        # Détermination automatique du rôle
        if len(enfants_data) > 0:

            role = 'parent'

        elif matricule:

            role = 'enseignant'

        else:

            role = 'admin'

        # Création de l'utilisateur
        utilisateur = Utilisateur(
            **validated_data,
            role=role
        )

        # IMPORTANT :
        # on ne met jamais le mot de passe
        # directement dans la base.
        utilisateur.set_password(password)

        utilisateur.save()

        # Création des enfants
        for enfant_data in enfants_data:

            enfant = Enfant.objects.create(
                **enfant_data
            )

            utilisateur.enfant.add(
                enfant
            )

        return utilisateur


class ConnexionSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        email = attrs.get('email')
        password = attrs.get('password')

        utilisateur = authenticate(
            username=email,
            password=password
        )

        if utilisateur is None:

            raise serializers.ValidationError(
                "Email ou mot de passe incorrect."
            )

        if not utilisateur.is_active:

            raise serializers.ValidationError(
                "Ce compte est désactivé."
            )

        token, created = Token.objects.get_or_create(
            user=utilisateur
        )

        attrs['utilisateur'] = utilisateur
        attrs['token'] = token

        return attrs


    