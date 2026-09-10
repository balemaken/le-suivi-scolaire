
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Classe, Eleve, Matiere
from .serializer import (
    ClasseSerializer,
    EleveSerializer,
    MatiereSerializer,
    
)
from user.models import Utilisateur


# =========================================================
#                    CRUD CLASSE
# =========================================================

class ClasseAPIView(APIView):

    # GET : récupérer toutes les classes
    def get(self, request):
        classes = Classe.objects.all()
        serializer = ClasseSerializer(classes, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # POST : créer une classe
    def post(self, request):
        serializer = ClasseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ClasseDetailAPIView(APIView):

    # GET : récupérer une classe
    def get(self, request, id_classe):

        try:
            classe = Classe.objects.get(id_classe=id_classe)
        except Classe.DoesNotExist:
            return Response(
                {"erreur": "Classe introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ClasseSerializer(classe)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # PUT : modifier complètement une classe
    def put(self, request, id_classe):

        try:
            classe = Classe.objects.get(id_classe=id_classe)
        except Classe.DoesNotExist:
            return Response(
                {"erreur": "Classe introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ClasseSerializer(
            classe,
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

    # PATCH : modifier partiellement une classe
    def patch(self, request, id_classe):

        try:
            classe = Classe.objects.get(id_classe=id_classe)
        except Classe.DoesNotExist:
            return Response(
                {"erreur": "Classe introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ClasseSerializer(
            classe,
            data=request.data,
            partial=True
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

    # DELETE : supprimer une classe
    def delete(self, request, id_classe):

        try:
            classe = Classe.objects.get(id_classe=id_classe)
        except Classe.DoesNotExist:
            return Response(
                {"erreur": "Classe introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        classe.delete()

        return Response(
            {"message": "Classe supprimée avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )


# =========================================================
#                    CRUD ELEVE
# =========================================================

class EleveAPIView(APIView):

    # GET : récupérer tous les élèves
    def get(self, request):
        eleves = Eleve.objects.all()
        serializer = EleveSerializer(eleves, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # POST : créer un élève
    def post(self, request):
        serializer = EleveSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class EleveDetailAPIView(APIView):

    # GET : récupérer un élève
    def get(self, request, id_eleve):

        try:
            eleve = Eleve.objects.get(id_eleve=id_eleve)
        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EleveSerializer(eleve)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # PUT : modifier complètement un élève
    def put(self, request, id_eleve):

        try:
            eleve = Eleve.objects.get(id_eleve=id_eleve)
        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EleveSerializer(
            eleve,
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

    # PATCH : modifier partiellement un élève
    def patch(self, request, id_eleve):

        try:
            eleve = Eleve.objects.get(id_eleve=id_eleve)
        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EleveSerializer(
            eleve,
            data=request.data,
            partial=True
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

    # DELETE : supprimer un élève
    def delete(self, request, id_eleve):

        try:
            eleve = Eleve.objects.get(id_eleve=id_eleve)
        except Eleve.DoesNotExist:
            return Response(
                {"erreur": "Élève introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        eleve.delete()

        return Response(
            {"message": "Élève supprimé avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )


# =========================================================
#             RECUPERER LES ELEVES D'UNE CLASSE
# =========================================================

class ElevesParClasseAPIView(APIView):

    def get(self, request, id_classe):

        try:
            classe = Classe.objects.get(id_classe=id_classe)
        except Classe.DoesNotExist:
            return Response(
                {"erreur": "Classe introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        eleves = Eleve.objects.filter(classe=classe)

        serializer = EleveSerializer(
            eleves,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# =========================================================
#                    CRUD MATIERE
# =========================================================

class MatiereAPIView(APIView):

    # GET : récupérer toutes les matières
    def get(self, request):
        matieres = Matiere.objects.all()
        serializer = MatiereSerializer(
            matieres,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # POST : créer une matière
    def post(self, request):

        serializer = MatiereSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class MatiereDetailAPIView(APIView):

    # GET : récupérer une matière
    def get(self, request, id_matiere):

        try:
            matiere = Matiere.objects.get(
                id_matiere=id_matiere
            )
        except Matiere.DoesNotExist:
            return Response(
                {"erreur": "Matière introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MatiereSerializer(matiere)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # PUT : modifier complètement une matière
    def put(self, request, id_matiere):

        try:
            matiere = Matiere.objects.get(
                id_matiere=id_matiere
            )
        except Matiere.DoesNotExist:
            return Response(
                {"erreur": "Matière introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MatiereSerializer(
            matiere,
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

    # PATCH : modifier partiellement une matière
    def patch(self, request, id_matiere):

        try:
            matiere = Matiere.objects.get(
                id_matiere=id_matiere
            )
        except Matiere.DoesNotExist:
            return Response(
                {"erreur": "Matière introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MatiereSerializer(
            matiere,
            data=request.data,
            partial=True
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

    # DELETE : supprimer une matière
    def delete(self, request, id_matiere):

        try:
            matiere = Matiere.objects.get(
                id_matiere=id_matiere
            )
        except Matiere.DoesNotExist:
            return Response(
                {"erreur": "Matière introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        matiere.delete()

        return Response(
            {"message": "Matière supprimée avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )


# =========================================================
#             RECUPERER LES MATIERES D'UNE CLASSE
# =========================================================

class MatieresParClasseAPIView(APIView):

    def get(self, request, id_classe):

        try:
            classe = Classe.objects.get(
                id_classe=id_classe
            )
        except Classe.DoesNotExist:
            return Response(
                {"erreur": "Classe introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        matieres = Matiere.objects.filter(
            classe=classe
        )

        serializer = MatiereSerializer(
            matieres,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# =========================================================
#       AFFECTER UN ENSEIGNANT A UNE CLASSE
# =========================================================

class AffecterEnseignantClasseAPIView(APIView):

    # POST : affecter
    def post(self, request, id_classe):

        try:
            classe = Classe.objects.get(
                id_classe=id_classe
            )
        except Classe.DoesNotExist:
            return Response(
                {"erreur": "Classe introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        id_enseignant = request.data.get(
            'enseignant'
        )

        if not id_enseignant:
            return Response(
                {
                    "erreur":
                    "L'identifiant de l'enseignant est obligatoire."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            enseignant = Utilisateur.objects.get(
                id_utilisateur=id_enseignant,
                role='enseignant'
            )
        except Utilisateur.DoesNotExist:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        classe.enseignant = enseignant
        classe.save()

        serializer = ClasseSerializer(classe)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # DELETE : retirer l'enseignant de la classe
    def delete(self, request, id_classe):

        try:
            classe = Classe.objects.get(
                id_classe=id_classe
            )
        except Classe.DoesNotExist:
            return Response(
                {"erreur": "Classe introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        classe.enseignant = None
        classe.save()

        return Response(
            {
                "message":
                "Enseignant retiré de la classe avec succès."
            },
            status=status.HTTP_200_OK
        )


# =========================================================
#       AFFECTER UN ENSEIGNANT A UNE MATIERE
# =========================================================

class AffecterEnseignantMatiereAPIView(APIView):

    # POST : affecter
    def post(self, request, id_matiere):

        try:
            matiere = Matiere.objects.get(
                id_matiere=id_matiere
            )
        except Matiere.DoesNotExist:
            return Response(
                {"erreur": "Matière introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        id_enseignant = request.data.get(
            'enseignant'
        )

        if not id_enseignant:
            return Response(
                {
                    "erreur":
                    "L'identifiant de l'enseignant est obligatoire."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            enseignant = Utilisateur.objects.get(
                id_utilisateur=id_enseignant,
                role='enseignant'
            )
        except Utilisateur.DoesNotExist:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        matiere.enseignant = enseignant
        matiere.save()

        serializer = MatiereSerializer(matiere)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # DELETE : retirer l'enseignant de la matière
    def delete(self, request, id_matiere):

        try:
            matiere = Matiere.objects.get(
                id_matiere=id_matiere
            )
        except Matiere.DoesNotExist:
            return Response(
                {"erreur": "Matière introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        matiere.enseignant = None
        matiere.save()

        return Response(
            {
                "message":
                "Enseignant retiré de la matière avec succès."
            },
            status=status.HTTP_200_OK
        )






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import Utilisateur

from .models import (
    Classe,
    Eleve,
    Matiere,
    LiaisonParentEleve
)

from .serializer import (
    ParentSerializer,
    LiaisonParentEleveSerializer,
    CreerLiaisonSerializer
)


# ============================================================
# 1. LISTE DE TOUS LES PARENTS
# ============================================================

class ParentAPIView(APIView):

    def get(self, request):

        parents = Utilisateur.objects.filter(
            role='parent'
        )

        serializer = ParentSerializer(
            parents,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 2. DETAILS D'UN PARENT
# ============================================================

class ParentDetailAPIView(APIView):

    def get_object(self, id_utilisateur):
        try:
            return Utilisateur.objects.get(
                id_utilisateur=id_utilisateur,
                role='parent'
            )
        except Utilisateur.DoesNotExist:
            return None

    def get(self, request, id_utilisateur):
        parent = self.get_object(id_utilisateur)
        if not parent:
            return Response(
                {"erreur": "Parent introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ParentSerializer(parent)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id_utilisateur):
        parent = self.get_object(id_utilisateur)
        if not parent:
            return Response(
                {"erreur": "Parent introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Champs modifiables
        if 'nom' in request.data:
            parent.nom = request.data['nom']
        if 'prenom' in request.data:
            parent.prenom = request.data['prenom']
        if 'email' in request.data:
            new_email = request.data['email']
            # Vérifier unicité
            if Utilisateur.objects.filter(
                email=new_email
            ).exclude(id_utilisateur=parent.id_utilisateur).exists():
                return Response(
                    {"email": ["Cet email est déjà utilisé."]},
                    status=status.HTTP_400_BAD_REQUEST
                )
            parent.email = new_email
        if 'telephone' in request.data:
            parent.telephone = request.data['telephone']
        if 'is_active' in request.data:
            parent.is_active = bool(request.data['is_active'])

        parent.save()

        serializer = ParentSerializer(parent)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id_utilisateur):
        return self.put(request, id_utilisateur)

    def delete(self, request, id_utilisateur):
        parent = self.get_object(id_utilisateur)
        if not parent:
            return Response(
                {"erreur": "Parent introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )
        parent.delete()
        return Response(
            {"message": "Parent supprimé avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )


# ============================================================
# 3. LISTER LES ENFANTS ENREGISTRES PAR UN PARENT
# ============================================================

class EnfantsDuParentAPIView(APIView):

    def get(self, request, id_utilisateur):

        try:
            parent = Utilisateur.objects.get(
                id_utilisateur=id_utilisateur,
                role='parent'
            )

        except Utilisateur.DoesNotExist:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        enfants = parent.enfant.all()

        from .serializer import EnfantSerializer

        serializer = EnfantSerializer(
            enfants,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


# ============================================================
# 4. LIAISON PARENT -> ELEVE
# ============================================================

class LierParentEleveAPIView(APIView):

    def post(self, request, id_utilisateur):

        # ----------------------------------------------------
        # Vérifier que le parent existe
        # ----------------------------------------------------

        try:

            parent = Utilisateur.objects.get(
                id_utilisateur=id_utilisateur,
                role='parent'
            )

        except Utilisateur.DoesNotExist:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ----------------------------------------------------
        # Vérifier les données reçues
        # ----------------------------------------------------

        serializer = CreerLiaisonSerializer(
            data=request.data
        )

        if not serializer.is_valid():

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        # ----------------------------------------------------
        # Récupérer l'identifiant de l'élève
        # ----------------------------------------------------

        id_eleve = serializer.validated_data[
            'id_eleve'
        ]

        # ----------------------------------------------------
        # Vérifier que l'élève existe
        # ----------------------------------------------------

        try:

            eleve = Eleve.objects.get(
                id_eleve=id_eleve
            )

        except Eleve.DoesNotExist:

            return Response(
                {
                    "erreur": "Élève introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ----------------------------------------------------
        # Vérifier si la liaison existe déjà
        # ----------------------------------------------------

        liaison_existante = LiaisonParentEleve.objects.filter(
            parent=parent,
            eleve=eleve
        ).exists()

        if liaison_existante:

            return Response(
                {
                    "erreur":
                    "Ce parent est déjà lié à cet élève."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ----------------------------------------------------
        # Créer la liaison
        # ----------------------------------------------------

        liaison = LiaisonParentEleve.objects.create(
            parent=parent,
            eleve=eleve
        )

        # ----------------------------------------------------
        # Retourner la liaison créée
        # ----------------------------------------------------

        response_serializer = LiaisonParentEleveSerializer(
            liaison
        )

        return Response(
            {
                "message":
                "Le parent a été lié à l'élève avec succès.",

                "liaison":
                response_serializer.data
            },
            status=status.HTTP_201_CREATED
        )


# ============================================================
# 5. VOIR LES ELEVES LIES A UN PARENT
# ============================================================

class ElevesDuParentAPIView(APIView):

    def get(self, request, id_utilisateur):

        # ----------------------------------------------------
        # Vérifier le parent
        # ----------------------------------------------------

        try:

            parent = Utilisateur.objects.get(
                id_utilisateur=id_utilisateur,
                role='parent'
            )

        except Utilisateur.DoesNotExist:

            return Response(
                {
                    "erreur": "Parent introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ----------------------------------------------------
        # Récupérer les liaisons
        # ----------------------------------------------------

        liaisons = LiaisonParentEleve.objects.filter(
            parent=parent
        ).select_related(
            'eleve',
            'eleve__classe'
        )

        # ----------------------------------------------------
        # Préparer la réponse
        # ----------------------------------------------------

        resultats = []

        for liaison in liaisons:

            resultats.append(
                {
                    "id_liaison":
                    liaison.id_liaison,

                    "id_eleve":
                    liaison.eleve.id_eleve,

                    "nom":
                    liaison.eleve.nom,

                    "sexe":
                    liaison.eleve.sexe,

                    "classe":
                    liaison.eleve.classe.nom,

                    "id_classe":
                    liaison.eleve.classe.id_classe
                }
            )

        return Response(
            resultats,
            status=status.HTTP_200_OK
        )


# ============================================================
# 6. SUPPRIMER UNE LIAISON PARENT -> ELEVE
# ============================================================

class RetirerParentEleveAPIView(APIView):

    def delete(
        self,
        request,
        id_utilisateur,
        id_eleve
    ):

        # ----------------------------------------------------
        # Rechercher la liaison
        # ----------------------------------------------------

        try:

            liaison = LiaisonParentEleve.objects.get(
                parent__id_utilisateur=id_utilisateur,
                parent__role='parent',
                eleve__id_eleve=id_eleve
            )

        except LiaisonParentEleve.DoesNotExist:

            return Response(
                {
                    "erreur":
                    "Cette liaison n'existe pas."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ----------------------------------------------------
        # Supprimer la liaison
        # ----------------------------------------------------

        liaison.delete()

        return Response(
            {
                "message":
                "La liaison parent-élève a été supprimée."
            },
            status=status.HTTP_200_OK
        )























from .models import Classe, Eleve, Matiere, LiaisonParentEleve

# =========================================================
#                    ENSEIGNANTS
# =========================================================

class EnseignantsAPIView(APIView):
    """
    Liste tous les utilisateurs ayant le rôle 'enseignant'.
    """
    def get(self, request):
        enseignants = Utilisateur.objects.filter(role='enseignant')
        
        data = []
        for ens in enseignants:
            data.append({
                'id_utilisateur': ens.id_utilisateur,
                'nom': ens.nom,
                'prenom': ens.prenom,
                'email': ens.email,
                'telephone': ens.telephone,
                'matricule': ens.matricule,
            })
        
        return Response(data, status=status.HTTP_200_OK)

from user.models import Utilisateur, Enfant
# =========================================================
#                    LIAISONS PARENT-ÉLÈVE
# =========================================================

# class LiaisonsAPIView(APIView):
#     """
#     Liste toutes les liaisons parent-élève.
#     """
#     def get(self, request):
#         liaisons = LiaisonParentEleve.objects.select_related(
#             'parent', 'eleve', 'eleve__classe'
#         ).all()
        
#         data = []
#         for l in liaisons:
#             data.append({
#                 'id_liaison': l.id_liaison,
#                 'parent_id': l.parent.id_utilisateur,
#                 'parent_nom': f"{l.parent.prenom} {l.parent.nom}".strip(),
#                 'eleve_id': l.eleve.id_eleve,
#                 'eleve_nom': l.eleve.nom,
#                 'eleve_classe': l.eleve.classe.nom if l.eleve.classe else '',
#                 'date_liaison': l.date_liaison,
#             })
        
#         return Response(data, status=status.HTTP_200_OK)



# =========================================================
#                    LIAISONS PARENT-ÉLÈVE
# =========================================================

class LiaisonsAPIView(APIView):
    """
    Liste TOUTES les relations parent-enfant :
    - Liaisons réelles (LiaisonParentEleve) → type = 'lie'
    - Enfants déclarés à l'inscription (Enfant) → type = 'declare'
    """
    def get(self, request):
        data = []

        # =====================================================
        # 1. LIAISONS RÉELLES (parent ↔ élève)
        # =====================================================
        liaisons = LiaisonParentEleve.objects.select_related(
            'parent', 'eleve', 'eleve__classe'
        ).all()

        for l in liaisons:
            parent_nom = f"{l.parent.prenom} {l.parent.nom}".strip()
            data.append({
                'id': f'lie-{l.id_liaison}',
                'type': 'lie',
                'type_label': 'Lié',
                'parent_id': l.parent.id_utilisateur,
                'parent_nom': parent_nom,
                'eleve_id': l.eleve.id_eleve,
                'eleve_nom': l.eleve.nom,
                'eleve_classe': l.eleve.classe.nom if l.eleve.classe else '',
                'date': l.date_liaison,
                'id_liaison': l.id_liaison,
                'id_enfant': None,
            })

        # =====================================================
        # 2. ENFANTS DÉCLARÉS (parent → enfant)
        # =====================================================
        # On récupère tous les parents et leurs enfants déclarés
        parents = Utilisateur.objects.filter(role='parent').prefetch_related('enfant')

        for parent in parents:
            parent_nom = f"{parent.prenom} {parent.nom}".strip()
            for enfant in parent.enfant.all():
                data.append({
                    'id': f'declare-{enfant.id_enfant}',
                    'type': 'declare',
                    'type_label': 'Déclaré',
                    'parent_id': parent.id_utilisateur,
                    'parent_nom': parent_nom,
                    'eleve_id': enfant.id_enfant,
                    'eleve_nom': enfant.nom,
                    'eleve_classe': enfant.classe,   # texte libre (ex: "5ème")
                    'date': None,
                    'id_liaison': None,
                    'id_enfant': enfant.id_enfant,
                })

        return Response(data, status=status.HTTP_200_OK)


# =========================================================
#        SUPPRIMER UNE LIAISON OU UN ENFANT DÉCLARÉ
# =========================================================

class SupprimerLiaisonAPIView(APIView):
    """
    Supprime selon le type :
    - /api/liaisons/lie/<id>/ → supprime LiaisonParentEleve
    - /api/liaisons/declare/<id>/ → supprime Enfant
    """
    def delete(self, request, type_item, id_item):

        if type_item == 'lie':
            try:
                liaison = LiaisonParentEleve.objects.get(id_liaison=id_item)
                liaison.delete()
                return Response(
                    {"message": "Liaison supprimée avec succès."},
                    status=status.HTTP_200_OK
                )
            except LiaisonParentEleve.DoesNotExist:
                return Response(
                    {"erreur": "Liaison introuvable."},
                    status=status.HTTP_404_NOT_FOUND
                )

        elif type_item == 'declare':
            try:
                enfant = Enfant.objects.get(id_enfant=id_item)
                enfant.delete()
                return Response(
                    {"message": "Enfant déclaré supprimé avec succès."},
                    status=status.HTTP_200_OK
                )
            except Enfant.DoesNotExist:
                return Response(
                    {"erreur": "Enfant introuvable."},
                    status=status.HTTP_404_NOT_FOUND
                )

        return Response(
            {"erreur": "Type inconnu (attendu : 'lie' ou 'declare')."},
            status=status.HTTP_400_BAD_REQUEST
        )









    # =========================================================
#                    ENSEIGNANTS
# =========================================================

class EnseignantsAPIView(APIView):
    """
    Liste tous les utilisateurs ayant le rôle 'enseignant'.
    Renvoie aussi les classes et matières affectées + le statut.
    """
    def get(self, request):
        enseignants = Utilisateur.objects.filter(role='enseignant')
        
        data = []
        for ens in enseignants:
            # Classes où cet enseignant est responsable
            classes = Classe.objects.filter(
                enseignant=ens
            ).values_list('nom', flat=True)
            
            # Matières où cet enseignant est affecté
            matieres = Matiere.objects.filter(
                enseignant=ens
            ).values_list('nom', flat=True)
            
            data.append({
                'id_utilisateur': ens.id_utilisateur,
                'nom': ens.nom,
                'prenom': ens.prenom,
                'email': ens.email,
                'telephone': ens.telephone or '',
                'matricule': ens.matricule or '',
                'is_active': ens.is_active,
                'classes': list(classes),
                'matieres': list(matieres),
            })
        
        return Response(data, status=status.HTTP_200_OK)


class EnseignantDetailAPIView(APIView):
    """
    GET / PUT / PATCH / DELETE d'un enseignant.
    """
    def get_object(self, id_enseignant):
        try:
            return Utilisateur.objects.get(
                id_utilisateur=id_enseignant,
                role='enseignant'
            )
        except Utilisateur.DoesNotExist:
            return None

    def get(self, request, id_enseignant):
        ens = self.get_object(id_enseignant)
        if not ens:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        classes = Classe.objects.filter(enseignant=ens).values_list('nom', flat=True)
        matieres = Matiere.objects.filter(enseignant=ens).values_list('nom', flat=True)
        
        return Response({
            'id_utilisateur': ens.id_utilisateur,
            'nom': ens.nom,
            'prenom': ens.prenom,
            'email': ens.email,
            'telephone': ens.telephone or '',
            'matricule': ens.matricule or '',
            'is_active': ens.is_active,
            'classes': list(classes),
            'matieres': list(matieres),
        }, status=status.HTTP_200_OK)

    def put(self, request, id_enseignant):
        ens = self.get_object(id_enseignant)
        if not ens:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Champs modifiables
        if 'nom' in request.data:
            ens.nom = request.data['nom']
        if 'prenom' in request.data:
            ens.prenom = request.data['prenom']
        if 'email' in request.data:
            # Vérifier unicité
            if Utilisateur.objects.filter(
                email=request.data['email']
            ).exclude(id_utilisateur=ens.id_utilisateur).exists():
                return Response(
                    {"erreur": "Cet email est déjà utilisé."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            ens.email = request.data['email']
        if 'telephone' in request.data:
            ens.telephone = request.data['telephone']
        if 'matricule' in request.data:
            ens.matricule = request.data['matricule']
        if 'is_active' in request.data:
            ens.is_active = bool(request.data['is_active'])
        
        ens.save()
        
        return Response({
            'message': "Enseignant mis à jour avec succès.",
            'id_utilisateur': ens.id_utilisateur,
            'nom': ens.nom,
            'prenom': ens.prenom,
            'email': ens.email,
            'telephone': ens.telephone or '',
            'matricule': ens.matricule or '',
            'is_active': ens.is_active,
        }, status=status.HTTP_200_OK)

    def patch(self, request, id_enseignant):
        return self.put(request, id_enseignant)

    def delete(self, request, id_enseignant):
        ens = self.get_object(id_enseignant)
        if not ens:
            return Response(
                {"erreur": "Enseignant introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        ens.delete()
        return Response(
            {"message": "Enseignant supprimé avec succès."},
            status=status.HTTP_204_NO_CONTENT
        )