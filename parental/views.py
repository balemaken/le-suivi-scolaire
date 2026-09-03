from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import Utilisateur

from administration.models import (
    Eleve,
    LiaisonParentEleve
)

from enseignement.models import (
    Note,
    Absence,
    Remarque,
    Sanction,
    Bulletin
)

from .serializer import (
    ParentSerializer,
    EleveParentSerializer,
    LiaisonParentSerializer,
    NoteParentSerializer,
    AbsenceParentSerializer,
    RemarqueParentSerializer,
    SanctionParentSerializer,
    BulletinParentSerializer
)


# ============================================================
# FONCTION UTILITAIRE
# ============================================================

def recuperer_parent(id_parent):

    try:
        return Utilisateur.objects.get(
            id_utilisateur=id_parent,
            role='parent'
        )

    except Utilisateur.DoesNotExist:
        return None


# ============================================================
# 1. PROFIL DU PARENT
# ============================================================

class ParentProfilAPIView(APIView):

    def get(self, request, id_parent):

        parent = recuperer_parent(id_parent)

        if parent is None:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ParentSerializer(parent)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 2. LISTE DES ELEVES DU PARENT
# ============================================================

class ElevesParentAPIView(APIView):

    def get(self, request, id_parent):

        parent = recuperer_parent(id_parent)

        if parent is None:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        liaisons = LiaisonParentEleve.objects.filter(
            parent=parent
        ).select_related(
            'eleve',
            'eleve__classe'
        )

        resultats = []

        for liaison in liaisons:

            resultats.append(
                {
                    "id_liaison": liaison.id_liaison,
                    "id_eleve": liaison.eleve.id_eleve,
                    "nom": liaison.eleve.nom,
                    "sexe": liaison.eleve.sexe,
                    "id_classe": liaison.eleve.classe.id_classe,
                    "classe": liaison.eleve.classe.nom,
                    "date_liaison": liaison.date_liaison
                }
            )

        return Response(
            resultats,
            status=status.HTTP_200_OK
        )


# ============================================================
# 3. INFORMATIONS GENERALES DE L'ELEVE
# ============================================================

class EleveParentDetailAPIView(APIView):

    def get(
        self,
        request,
        id_parent,
        id_eleve
    ):

        parent = recuperer_parent(id_parent)

        if parent is None:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # Vérifier que l'élève appartient bien au parent
        liaison = LiaisonParentEleve.objects.filter(
            parent=parent,
            eleve_id=id_eleve
        ).select_related(
            'eleve',
            'eleve__classe'
        ).first()

        if liaison is None:

            return Response(
                {
                    "erreur":
                    "Vous n'êtes pas autorisé à consulter cet élève."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = EleveParentSerializer(
            liaison.eleve
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 4. NOTES DE L'ELEVE
# ============================================================

class NotesParentAPIView(APIView):

    def get(
        self,
        request,
        id_parent,
        id_eleve
    ):

        parent = recuperer_parent(id_parent)

        if parent is None:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # Vérification de la liaison
        if not LiaisonParentEleve.objects.filter(
            parent=parent,
            eleve_id=id_eleve
        ).exists():

            return Response(
                {
                    "erreur":
                    "Vous n'êtes pas autorisé à consulter cet élève."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        notes = Note.objects.filter(
            eleve_id=id_eleve
        ).select_related(
            'matiere'
        )

        serializer = NoteParentSerializer(
            notes,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 5. ABSENCES DE L'ELEVE
# ============================================================

class AbsencesParentAPIView(APIView):

    def get(
        self,
        request,
        id_parent,
        id_eleve
    ):

        parent = recuperer_parent(id_parent)

        if parent is None:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if not LiaisonParentEleve.objects.filter(
            parent=parent,
            eleve_id=id_eleve
        ).exists():

            return Response(
                {
                    "erreur":
                    "Vous n'êtes pas autorisé à consulter cet élève."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        absences = Absence.objects.filter(
            eleve_id=id_eleve
        ).select_related(
            'matiere'
        )

        serializer = AbsenceParentSerializer(
            absences,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 6. REMARQUES DE L'ELEVE
# ============================================================

class RemarquesParentAPIView(APIView):

    def get(
        self,
        request,
        id_parent,
        id_eleve
    ):

        parent = recuperer_parent(id_parent)

        if parent is None:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if not LiaisonParentEleve.objects.filter(
            parent=parent,
            eleve_id=id_eleve
        ).exists():

            return Response(
                {
                    "erreur":
                    "Vous n'êtes pas autorisé à consulter cet élève."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        remarques = Remarque.objects.filter(
            eleve_id=id_eleve
        )

        serializer = RemarqueParentSerializer(
            remarques,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 7. SANCTIONS DE L'ELEVE
# ============================================================

class SanctionsParentAPIView(APIView):

    def get(
        self,
        request,
        id_parent,
        id_eleve
    ):

        parent = recuperer_parent(id_parent)

        if parent is None:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if not LiaisonParentEleve.objects.filter(
            parent=parent,
            eleve_id=id_eleve
        ).exists():

            return Response(
                {
                    "erreur":
                    "Vous n'êtes pas autorisé à consulter cet élève."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        sanctions = Sanction.objects.filter(
            eleve_id=id_eleve
        )

        serializer = SanctionParentSerializer(
            sanctions,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 8. BULLETINS DE L'ELEVE
# ============================================================

class BulletinsParentAPIView(APIView):

    def get(
        self,
        request,
        id_parent,
        id_eleve
    ):

        parent = recuperer_parent(id_parent)

        if parent is None:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if not LiaisonParentEleve.objects.filter(
            parent=parent,
            eleve_id=id_eleve
        ).exists():

            return Response(
                {
                    "erreur":
                    "Vous n'êtes pas autorisé à consulter cet élève."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        bulletins = Bulletin.objects.filter(
            eleve_id=id_eleve
        )

        serializer = BulletinParentSerializer(
            bulletins,
            many=True,
            context={
                'request': request
            }
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 9. SUIVI COMPLET DE L'ELEVE
# ============================================================

class SuiviCompletEleveParentAPIView(APIView):

    def get(
        self,
        request,
        id_parent,
        id_eleve
    ):

        parent = recuperer_parent(id_parent)

        if parent is None:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # =====================================================
        # VERIFICATION DE LA LIAISON
        # =====================================================

        liaison = LiaisonParentEleve.objects.filter(
            parent=parent,
            eleve_id=id_eleve
        ).select_related(
            'eleve',
            'eleve__classe'
        ).first()

        if liaison is None:

            return Response(
                {
                    "erreur":
                    "Vous n'êtes pas autorisé à consulter cet élève."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        eleve = liaison.eleve

        # =====================================================
        # RECUPERATION
        # =====================================================

        notes = Note.objects.filter(
            eleve=eleve
        ).select_related(
            'matiere'
        )

        absences = Absence.objects.filter(
            eleve=eleve
        ).select_related(
            'matiere'
        )

        remarques = Remarque.objects.filter(
            eleve=eleve
        )

        sanctions = Sanction.objects.filter(
            eleve=eleve
        )

        bulletins = Bulletin.objects.filter(
            eleve=eleve
        )

        # =====================================================
        # SERIALIZERS
        # =====================================================

        eleve_serializer = EleveParentSerializer(
            eleve
        )

        notes_serializer = NoteParentSerializer(
            notes,
            many=True
        )

        absences_serializer = AbsenceParentSerializer(
            absences,
            many=True
        )

        remarques_serializer = RemarqueParentSerializer(
            remarques,
            many=True
        )

        sanctions_serializer = SanctionParentSerializer(
            sanctions,
            many=True
        )

        bulletins_serializer = BulletinParentSerializer(
            bulletins,
            many=True,
            context={
                'request': request
            }
        )

        # =====================================================
        # REPONSE
        # =====================================================

        return Response(
            {
                "eleve": eleve_serializer.data,

                "notes": notes_serializer.data,

                "absences": absences_serializer.data,

                "remarques": remarques_serializer.data,

                "sanctions": sanctions_serializer.data,

                "bulletins": bulletins_serializer.data
            },
            status=status.HTTP_200_OK
        )