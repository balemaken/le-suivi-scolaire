from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from user.models import Utilisateur

from administration.models import (
    Classe,
    Eleve,
    Matiere
)

from .models import (
    Note,
    Absence,
    Remarque,
    Sanction,
    Bulletin
)

from .serializer import (
    ClasseEnseignantSerializer,
    EleveEnseignantSerializer,
    MatiereEnseignantSerializer,
    NoteSerializer,
    AbsenceSerializer,
    RemarqueSerializer,
    SanctionSerializer,
    BulletinSerializer
)


# ============================================================
# FONCTION UTILITAIRE
# ============================================================

def recuperer_enseignant(id_enseignant):

    try:
        return Utilisateur.objects.get(
            id_utilisateur=id_enseignant,
            role='enseignant'
        )

    except Utilisateur.DoesNotExist:
        return None


# ============================================================
# 1. CLASSES DE L'ENSEIGNANT
# ============================================================

class ClassesEnseignantAPIView(APIView):

    def get(self, request, id_enseignant):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        classes = Classe.objects.filter(
            enseignant=enseignant
        ).order_by('nom')

        serializer = ClasseEnseignantSerializer(
            classes,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 2. DETAILS D'UNE CLASSE
# ============================================================

class ClasseEnseignantDetailAPIView(APIView):

    def get(
        self,
        request,
        id_enseignant,
        id_classe
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:

            classe = Classe.objects.get(
                id_classe=id_classe,
                enseignant=enseignant
            )

        except Classe.DoesNotExist:

            return Response(
                {
                    "erreur":
                    "Cette classe n'est pas affectée à cet enseignant."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ClasseEnseignantSerializer(
            classe
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 3. ELEVES D'UNE CLASSE
# ============================================================

class ElevesClasseEnseignantAPIView(APIView):

    def get(
        self,
        request,
        id_enseignant,
        id_classe
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:

            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Vérifier que la classe appartient à l'enseignant
        if not Classe.objects.filter(
            id_classe=id_classe,
            enseignant=enseignant
        ).exists():

            return Response(
                {
                    "erreur":
                    "Cette classe n'est pas affectée à cet enseignant."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        eleves = Eleve.objects.filter(
            classe_id=id_classe
        ).order_by('nom')

        serializer = EleveEnseignantSerializer(
            eleves,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 4. MATIERES ENSEIGNEES PAR L'ENSEIGNANT DANS UNE CLASSE
# ============================================================

class MatieresClasseEnseignantAPIView(APIView):

    def get(
        self,
        request,
        id_enseignant,
        id_classe
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:

            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Vérifier la classe
        if not Classe.objects.filter(
            id_classe=id_classe,
            enseignant=enseignant
        ).exists():

            return Response(
                {
                    "erreur":
                    "Cette classe n'est pas affectée à cet enseignant."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        matieres = Matiere.objects.filter(
            classe_id=id_classe,
            enseignant=enseignant
        ).order_by('nom')

        serializer = MatiereEnseignantSerializer(
            matieres,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 5. NOTES D'UN ELEVE
# ============================================================

class NotesEleveAPIView(APIView):

    def get(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(
                id_eleve=id_eleve
            )

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        # L'enseignant doit être responsable de la classe
        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {
                    "erreur":
                    "Cet élève n'appartient pas à une classe "
                    "gérée par cet enseignant."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        notes = Note.objects.filter(
            eleve=eleve,
            enseignant=enseignant
        ).select_related('matiere')

        serializer = NoteSerializer(
            notes,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(
                id_eleve=id_eleve
            )

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Vérifier classe
        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {
                    "erreur":
                    "Vous ne pouvez pas gérer cet élève."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        # Vérifier matière
        id_matiere = request.data.get('matiere')

        if not id_matiere:

            return Response(
                {"erreur": "La matière est obligatoire."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            matiere = Matiere.objects.get(
                id_matiere=id_matiere,
                classe=eleve.classe,
                enseignant=enseignant
            )

        except Matiere.DoesNotExist:

            return Response(
                {
                    "erreur":
                    "Cette matière n'est pas enseignée "
                    "par cet enseignant dans cette classe."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = NoteSerializer(
            data=request.data
        )

        if serializer.is_valid():

            note = serializer.save(
                eleve=eleve,
                enseignant=enseignant
            )

            return Response(
                NoteSerializer(note).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# ============================================================
# 6. DETAIL / MODIFICATION / SUPPRESSION NOTE
# ============================================================

class NoteDetailAPIView(APIView):

    def get_object(
        self,
        id_enseignant,
        id_note
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return None, None

        try:

            note = Note.objects.select_related(
                'eleve',
                'matiere'
            ).get(
                id_note=id_note,
                enseignant=enseignant
            )

            return enseignant, note

        except Note.DoesNotExist:

            return enseignant, None

    def get(
        self,
        request,
        id_enseignant,
        id_note
    ):

        enseignant, note = self.get_object(
            id_enseignant,
            id_note
        )

        if not enseignant:

            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not note:

            return Response(
                {"erreur": "Note introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            NoteSerializer(note).data
        )

    def put(
        self,
        request,
        id_enseignant,
        id_note
    ):

        enseignant, note = self.get_object(
            id_enseignant,
            id_note
        )

        if not enseignant:

            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not note:

            return Response(
                {"erreur": "Note introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Vérifier nouvelle matière
        id_matiere = request.data.get('matiere')

        if id_matiere:

            if not Matiere.objects.filter(
                id_matiere=id_matiere,
                classe=note.eleve.classe,
                enseignant=enseignant
            ).exists():

                return Response(
                    {
                        "erreur":
                        "Cette matière n'est pas enseignée "
                        "par cet enseignant dans cette classe."
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

        serializer = NoteSerializer(
            note,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(
        self,
        request,
        id_enseignant,
        id_note
    ):

        enseignant, note = self.get_object(
            id_enseignant,
            id_note
        )

        if not enseignant:

            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not note:

            return Response(
                {"erreur": "Note introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        note.delete()

        return Response(
            {
                "message":
                "Note supprimée avec succès."
            },
            status=status.HTTP_204_NO_CONTENT
        )


# ============================================================
# 7. ABSENCES
# ============================================================

class AbsencesEleveAPIView(APIView):

    def get(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(id_eleve=id_eleve)

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {"erreur": "Vous ne pouvez pas gérer cet élève."},
                status=status.HTTP_403_FORBIDDEN
            )

        absences = Absence.objects.filter(
            eleve=eleve,
            enseignant=enseignant
        ).select_related('matiere')

        return Response(
            AbsenceSerializer(
                absences,
                many=True
            ).data
        )

    def post(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(id_eleve=id_eleve)

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {"erreur": "Vous ne pouvez pas gérer cet élève."},
                status=status.HTTP_403_FORBIDDEN
            )

        id_matiere = request.data.get('matiere')

        if not Matiere.objects.filter(
            id_matiere=id_matiere,
            classe=eleve.classe,
            enseignant=enseignant
        ).exists():

            return Response(
                {
                    "erreur":
                    "Cette matière n'est pas enseignée "
                    "par cet enseignant."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = AbsenceSerializer(
            data=request.data
        )

        if serializer.is_valid():

            absence = serializer.save(
                eleve=eleve,
                enseignant=enseignant
            )

            return Response(
                AbsenceSerializer(absence).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# ============================================================
# 8. DETAIL ABSENCE
# ============================================================

class AbsenceDetailAPIView(APIView):

    def get_object(
        self,
        id_enseignant,
        id_absence
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return None, None

        try:
            absence = Absence.objects.get(
                id_absence=id_absence,
                enseignant=enseignant
            )

            return enseignant, absence

        except Absence.DoesNotExist:

            return enseignant, None

    def get(
        self,
        request,
        id_enseignant,
        id_absence
    ):

        enseignant, absence = self.get_object(
            id_enseignant,
            id_absence
        )

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not absence:
            return Response(
                {"erreur": "Absence introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            AbsenceSerializer(absence).data
        )

    def put(
        self,
        request,
        id_enseignant,
        id_absence
    ):

        enseignant, absence = self.get_object(
            id_enseignant,
            id_absence
        )

        if not absence:
            return Response(
                {"erreur": "Absence introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AbsenceSerializer(
            absence,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(
        self,
        request,
        id_enseignant,
        id_absence
    ):

        enseignant, absence = self.get_object(
            id_enseignant,
            id_absence
        )

        if not absence:
            return Response(
                {"erreur": "Absence introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        absence.delete()

        return Response(
            {"message": "Absence supprimée avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )


# ============================================================
# 9. REMARQUES
# ============================================================

class RemarquesEleveAPIView(APIView):

    def get(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(id_eleve=id_eleve)

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {"erreur": "Vous ne pouvez pas gérer cet élève."},
                status=status.HTTP_403_FORBIDDEN
            )

        remarques = Remarque.objects.filter(
            eleve=eleve,
            enseignant=enseignant
        )

        return Response(
            RemarqueSerializer(
                remarques,
                many=True
            ).data
        )

    def post(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(id_eleve=id_eleve)

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {"erreur": "Vous ne pouvez pas gérer cet élève."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = RemarqueSerializer(
            data=request.data
        )

        if serializer.is_valid():

            remarque = serializer.save(
                eleve=eleve,
                enseignant=enseignant
            )

            return Response(
                RemarqueSerializer(remarque).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# ============================================================
# 10. DETAIL REMARQUE
# ============================================================

class RemarqueDetailAPIView(APIView):

    def get_object(
        self,
        id_enseignant,
        id_remarque
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return None, None

        try:

            remarque = Remarque.objects.get(
                id_remarque=id_remarque,
                enseignant=enseignant
            )

            return enseignant, remarque

        except Remarque.DoesNotExist:

            return enseignant, None

    def get(
        self,
        request,
        id_enseignant,
        id_remarque
    ):

        enseignant, remarque = self.get_object(
            id_enseignant,
            id_remarque
        )

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not remarque:
            return Response(
                {"erreur": "Remarque introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            RemarqueSerializer(remarque).data
        )

    def put(
        self,
        request,
        id_enseignant,
        id_remarque
    ):

        enseignant, remarque = self.get_object(
            id_enseignant,
            id_remarque
        )

        if not remarque:
            return Response(
                {"erreur": "Remarque introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RemarqueSerializer(
            remarque,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(
        self,
        request,
        id_enseignant,
        id_remarque
    ):

        enseignant, remarque = self.get_object(
            id_enseignant,
            id_remarque
        )

        if not remarque:
            return Response(
                {"erreur": "Remarque introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        remarque.delete()

        return Response(
            {"message": "Remarque supprimée avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )


# ============================================================
# 11. SANCTIONS
# ============================================================

class SanctionsEleveAPIView(APIView):

    def get(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(id_eleve=id_eleve)

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {"erreur": "Vous ne pouvez pas gérer cet élève."},
                status=status.HTTP_403_FORBIDDEN
            )

        sanctions = Sanction.objects.filter(
            eleve=eleve,
            enseignant=enseignant
        )

        return Response(
            SanctionSerializer(
                sanctions,
                many=True
            ).data
        )

    def post(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(id_eleve=id_eleve)

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {"erreur": "Vous ne pouvez pas gérer cet élève."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = SanctionSerializer(
            data=request.data
        )

        if serializer.is_valid():

            sanction = serializer.save(
                eleve=eleve,
                enseignant=enseignant
            )

            return Response(
                SanctionSerializer(sanction).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# ============================================================
# 12. DETAIL SANCTION
# ============================================================

class SanctionDetailAPIView(APIView):

    def get_object(
        self,
        id_enseignant,
        id_sanction
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return None, None

        try:

            sanction = Sanction.objects.get(
                id_sanction=id_sanction,
                enseignant=enseignant
            )

            return enseignant, sanction

        except Sanction.DoesNotExist:

            return enseignant, None

    def get(
        self,
        request,
        id_enseignant,
        id_sanction
    ):

        enseignant, sanction = self.get_object(
            id_enseignant,
            id_sanction
        )

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not sanction:
            return Response(
                {"erreur": "Sanction introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            SanctionSerializer(sanction).data
        )

    def put(
        self,
        request,
        id_enseignant,
        id_sanction
    ):

        enseignant, sanction = self.get_object(
            id_enseignant,
            id_sanction
        )

        if not sanction:
            return Response(
                {"erreur": "Sanction introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SanctionSerializer(
            sanction,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(
        self,
        request,
        id_enseignant,
        id_sanction
    ):

        enseignant, sanction = self.get_object(
            id_enseignant,
            id_sanction
        )

        if not sanction:
            return Response(
                {"erreur": "Sanction introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        sanction.delete()

        return Response(
            {"message": "Sanction supprimée avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )


# ============================================================
# 13. BULLETINS
# ============================================================

class BulletinsEleveAPIView(APIView):

    parser_classes = [
        MultiPartParser,
        FormParser
    ]

    def get(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(id_eleve=id_eleve)

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {"erreur": "Vous ne pouvez pas gérer cet élève."},
                status=status.HTTP_403_FORBIDDEN
            )

        bulletins = Bulletin.objects.filter(
            eleve=eleve,
            enseignant=enseignant
        )

        return Response(
            BulletinSerializer(
                bulletins,
                many=True,
                context={'request': request}
            ).data
        )

    def post(
        self,
        request,
        id_enseignant,
        id_eleve
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            eleve = Eleve.objects.select_related(
                'classe'
            ).get(id_eleve=id_eleve)

        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if eleve.classe.enseignant_id != enseignant.id_utilisateur:

            return Response(
                {"erreur": "Vous ne pouvez pas gérer cet élève."},
                status=status.HTTP_403_FORBIDDEN
            )

        if 'fichier' not in request.FILES:

            return Response(
                {
                    "erreur":
                    "Le fichier du bulletin est obligatoire."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BulletinSerializer(
            data=request.data
        )

        if serializer.is_valid():

            bulletin = serializer.save(
                eleve=eleve,
                enseignant=enseignant
            )

            return Response(
                BulletinSerializer(
                    bulletin,
                    context={'request': request}
                ).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# ============================================================
# 14. DETAIL BULLETIN
# ============================================================

class BulletinDetailAPIView(APIView):

    parser_classes = [
        MultiPartParser,
        FormParser
    ]

    def get_object(
        self,
        id_enseignant,
        id_bulletin
    ):

        enseignant = recuperer_enseignant(id_enseignant)

        if not enseignant:
            return None, None

        try:

            bulletin = Bulletin.objects.get(
                id_bulletin=id_bulletin,
                enseignant=enseignant
            )

            return enseignant, bulletin

        except Bulletin.DoesNotExist:

            return enseignant, None

    def get(
        self,
        request,
        id_enseignant,
        id_bulletin
    ):

        enseignant, bulletin = self.get_object(
            id_enseignant,
            id_bulletin
        )

        if not enseignant:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not bulletin:
            return Response(
                {"erreur": "Bulletin introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            BulletinSerializer(
                bulletin,
                context={'request': request}
            ).data
        )

    def put(
        self,
        request,
        id_enseignant,
        id_bulletin
    ):

        enseignant, bulletin = self.get_object(
            id_enseignant,
            id_bulletin
        )

        if not bulletin:
            return Response(
                {"erreur": "Bulletin introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BulletinSerializer(
            bulletin,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                BulletinSerializer(
                    bulletin,
                    context={'request': request}
                ).data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(
        self,
        request,
        id_enseignant,
        id_bulletin
    ):

        enseignant, bulletin = self.get_object(
            id_enseignant,
            id_bulletin
        )

        if not bulletin:
            return Response(
                {"erreur": "Bulletin introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        bulletin.delete()

        return Response(
            {"message": "Bulletin supprimé avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )

