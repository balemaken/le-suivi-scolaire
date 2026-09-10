
from django.urls import path

from .views import (
    ClasseAPIView,
    ClasseDetailAPIView,

    EleveAPIView,
    EleveDetailAPIView,
    ElevesParClasseAPIView,

    MatiereAPIView,
    MatiereDetailAPIView,
    MatieresParClasseAPIView,

    AffecterEnseignantClasseAPIView,
    AffecterEnseignantMatiereAPIView,


    ParentAPIView, 
    ParentDetailAPIView,
      EnfantsDuParentAPIView,
        LierParentEleveAPIView,
          ElevesDuParentAPIView,
            RetirerParentEleveAPIView,

            EnseignantsAPIView,   # ← Ajouter
    LiaisonsAPIView,


     EnseignantDetailAPIView,

     SupprimerLiaisonAPIView
)



urlpatterns = [

    # =====================================================
    # CLASSES
    # =====================================================

    # GET toutes les classes
    # POST créer une classe
    path(
        'classes/',
        ClasseAPIView.as_view(),
        name='classes'
    ),

    # GET / PUT / PATCH / DELETE une classe
    path(
        'classes/<int:id_classe>/',
        ClasseDetailAPIView.as_view(),
        name='classe_detail'
    ),

    # GET les élèves d'une classe
    path(
        'classes/<int:id_classe>/eleves/',
        ElevesParClasseAPIView.as_view(),
        name='eleves_par_classe'
    ),

    # Affecter / retirer enseignant d'une classe
    path(
        'classes/<int:id_classe>/enseignant/',
        AffecterEnseignantClasseAPIView.as_view(),
        name='affecter_enseignant_classe'
    ),


    # =====================================================
    # ELEVES
    # =====================================================

    # GET tous les élèves
    # POST créer un élève
    path(
        'eleves/',
        EleveAPIView.as_view(),
        name='eleves'
    ),

    # GET / PUT / PATCH / DELETE un élève
    path(
        'eleves/<int:id_eleve>/',
        EleveDetailAPIView.as_view(),
        name='eleve_detail'
    ),


    # =====================================================
    # MATIERES
    # =====================================================

    # GET toutes les matières
    # POST créer une matière
    path(
        'matieres/',
        MatiereAPIView.as_view(),
        name='matieres'
    ),

    # GET / PUT / PATCH / DELETE une matière
    path(
        'matieres/<int:id_matiere>/',
        MatiereDetailAPIView.as_view(),
        name='matiere_detail'
    ),

    # GET les matières d'une classe
    path(
        'classes/<int:id_classe>/matieres/',
        MatieresParClasseAPIView.as_view(),
        name='matieres_par_classe'
    ),

    # Affecter / retirer enseignant d'une matière
    path(
        'matieres/<int:id_matiere>/enseignant/',
        AffecterEnseignantMatiereAPIView.as_view(),
        name='affecter_enseignant_matiere'
    ),



# Liste des parents
 path( 'parents/', ParentAPIView.as_view(), name='parents' ),
   # Détails d'un parent
 path( 'parents/<int:id_utilisateur>/', ParentDetailAPIView.as_view(), name='parent_detail' ),
   # Enfants enregistrés par le parent 
path( 'parents/<int:id_utilisateur>/enfants/', EnfantsDuParentAPIView.as_view(), name='enfants_parent' ),
 # Lier parent et élève
 path( 'parents/<int:id_utilisateur>/liaison/', LierParentEleveAPIView.as_view(), name='lier_parent_eleve' ),
   # Élèves liés au parent
 path( 'parents/<int:id_utilisateur>/eleves/', ElevesDuParentAPIView.as_view(), name='eleves_parent' ),
 # Supprimer une liaison
  path( 'parents/<int:id_utilisateur>/liaison/<int:id_eleve>/', RetirerParentEleveAPIView.as_view(), name='retirer_parent_eleve' ),






    path(
        'enseignants/',
        EnseignantsAPIView.as_view(),
        name='api_enseignants'
    ),

    # =====================================================
    # ENSEIGNANTS
    # =====================================================
    path(
        'enseignants/',
        EnseignantsAPIView.as_view(),
        name='api_enseignants'
    ),

    # DÉTAIL D'UN ENSEIGNANT (GET/PUT/PATCH/DELETE)
    path(
        'enseignants/<int:id_enseignant>/',
        EnseignantDetailAPIView.as_view(),
        name='api_enseignant_detail'
    ),






    # =====================================================
    # LIAISONS
    # =====================================================
    # path(
    #     'liaisons/',
    #     LiaisonsAPIView.as_view(),
    #     name='api_liaisons'
    # ),


    # =====================================================
    # LIAISONS
    # =====================================================
    path(
        'liaisons/',
        LiaisonsAPIView.as_view(),
        name='api_liaisons'
    ),

    # Suppression d'une liaison (lie) ou d'un enfant déclaré (declare)
    path(
        'liaisons/<str:type_item>/<int:id_item>/',
        SupprimerLiaisonAPIView.as_view(),
        name='api_supprimer_liaison'
    ),


]

