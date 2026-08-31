from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializer import (
    InscriptionSerializer,
    ConnexionSerializer,
    EnfantSerializer
)


class InscriptionAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = InscriptionSerializer(
            data=request.data
        )

        if serializer.is_valid():

            utilisateur = serializer.save()

            token, created = Token.objects.get_or_create(
                user=utilisateur
            )

            return Response(
                {
                    'message': 'Inscription réussie.',
                    'utilisateur': {
                        'id_utilisateur': utilisateur.id_utilisateur,
                        'nom': utilisateur.nom,
                        'prenom': utilisateur.prenom,
                        'email': utilisateur.email,
                        'telephone': utilisateur.telephone,
                        'sexe': utilisateur.sexe,
                        'role': utilisateur.role,
                    },
                    'token': token.key
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ConnexionAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = ConnexionSerializer(
            data=request.data
        )

        if serializer.is_valid():

            utilisateur = serializer.validated_data[
                'utilisateur'
            ]

            token = serializer.validated_data[
                'token'
            ]

            return Response(
                {
                    'message': 'Connexion réussie.',
                    'token': token.key,
                    'utilisateur': {
                        'id_utilisateur':
                            utilisateur.id_utilisateur,
                        'nom':
                            utilisateur.nom,
                        'prenom':
                            utilisateur.prenom,
                        'email':
                            utilisateur.email,
                        'role':
                            utilisateur.role,
                    }
                },
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_401_UNAUTHORIZED
        )


class ProfilAPIView(APIView):

    authentication_classes = [
        TokenAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        utilisateur = request.user

        enfants = utilisateur.enfant.all()

        enfants_data = EnfantSerializer(
            enfants,
            many=True
        ).data

        return Response(
            {
                'id_utilisateur':
                    utilisateur.id_utilisateur,

                'nom':
                    utilisateur.nom,

                'prenom':
                    utilisateur.prenom,

                'email':
                    utilisateur.email,

                'telephone':
                    utilisateur.telephone,

                'sexe':
                    utilisateur.sexe,

                'role':
                    utilisateur.role,

                'matricule':
                    utilisateur.matricule,

                'enfants':
                    enfants_data,
            }
        )


class DeconnexionAPIView(APIView):

    authentication_classes = [
        TokenAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        try:

            request.user.auth_token.delete()

        except Token.DoesNotExist:

            pass

        return Response(
            {
                'message':
                    'Déconnexion réussie.'
            },
            status=status.HTTP_200_OK
        )