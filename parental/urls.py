from django.urls import path

from .views import (
    ParentProfilAPIView,
    ElevesParentAPIView,
    EleveParentDetailAPIView,

    NotesParentAPIView,
    AbsencesParentAPIView,
    RemarquesParentAPIView,
    SanctionsParentAPIView,
    BulletinsParentAPIView,

    SuiviCompletEleveParentAPIView
)


urlpatterns = [

    # ========================================================
    # PROFIL DU PARENT
    # ========================================================

    path(
        'parents/<int:id_parent>/',
        ParentProfilAPIView.as_view(),
        name='parent_profil'
    ),


    # ========================================================
    # ELEVES DU PARENT
    # ========================================================

    path(
        'parents/<int:id_parent>/eleves/',
        ElevesParentAPIView.as_view(),
        name='parent_eleves'
    ),


    # ========================================================
    # INFORMATIONS D'UN ELEVE
    # ========================================================

    path(
        'parents/<int:id_parent>/eleves/<int:id_eleve>/',
        EleveParentDetailAPIView.as_view(),
        name='parent_eleve_detail'
    ),


    # ========================================================
    # NOTES
    # ========================================================

    path(
        'parents/<int:id_parent>/eleves/<int:id_eleve>/notes/',
        NotesParentAPIView.as_view(),
        name='parent_notes'
    ),


    # ========================================================
    # ABSENCES
    # ========================================================

    path(
        'parents/<int:id_parent>/eleves/<int:id_eleve>/absences/',
        AbsencesParentAPIView.as_view(),
        name='parent_absences'
    ),


    # ========================================================
    # REMARQUES
    # ========================================================

    path(
        'parents/<int:id_parent>/eleves/<int:id_eleve>/remarques/',
        RemarquesParentAPIView.as_view(),
        name='parent_remarques'
    ),


    # ========================================================
    # SANCTIONS
    # ========================================================

    path(
        'parents/<int:id_parent>/eleves/<int:id_eleve>/sanctions/',
        SanctionsParentAPIView.as_view(),
        name='parent_sanctions'
    ),


    # ========================================================
    # BULLETINS
    # ========================================================

    path(
        'parents/<int:id_parent>/eleves/<int:id_eleve>/bulletins/',
        BulletinsParentAPIView.as_view(),
        name='parent_bulletins'
    ),


    # ========================================================
    # SUIVI COMPLET
    # ========================================================

    path(
        'parents/<int:id_parent>/eleves/<int:id_eleve>/suivi/',
        SuiviCompletEleveParentAPIView.as_view(),
        name='parent_suivi_complet'
    ),
]