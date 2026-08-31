from django.urls import path

from .views import (
    InscriptionAPIView,
    ConnexionAPIView,
    ProfilAPIView,
    DeconnexionAPIView
)


urlpatterns = [

    path(
        'inscription/',
        InscriptionAPIView.as_view(),
        name='api_inscription'
    ),

    path(
        'connexion/',
        ConnexionAPIView.as_view(),
        name='api_connexion'
    ),

    path(
        'profil/',
        ProfilAPIView.as_view(),
        name='api_profil'
    ),

    path(
        'deconnexion/',
        DeconnexionAPIView.as_view(),
        name='api_deconnexion'
    ),
]