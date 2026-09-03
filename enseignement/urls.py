
from django.urls import path

from .views import (
    ClassesEnseignantAPIView,
    ClasseEnseignantDetailAPIView,
    ElevesClasseEnseignantAPIView,
    MatieresClasseEnseignantAPIView,

    NotesEleveAPIView,
    NoteDetailAPIView,

    AbsencesEleveAPIView,
    AbsenceDetailAPIView,

    RemarquesEleveAPIView,
    RemarqueDetailAPIView,

    SanctionsEleveAPIView,
    SanctionDetailAPIView,

    BulletinsEleveAPIView,
    BulletinDetailAPIView,
)


urlpatterns = [

    # ========================================================
    # CLASSES
    # ========================================================

    path(
        'enseignants/<int:id_enseignant>/classes/',
        ClassesEnseignantAPIView.as_view(),
        name='classes_enseignant'
    ),

    path(
        'enseignants/<int:id_enseignant>/classes/<int:id_classe>/',
        ClasseEnseignantDetailAPIView.as_view(),
        name='classe_enseignant_detail'
    ),

    # ========================================================
    # ELEVES D'UNE CLASSE
    # ========================================================

    path(
        'enseignants/<int:id_enseignant>/classes/<int:id_classe>/eleves/',
        ElevesClasseEnseignantAPIView.as_view(),
        name='eleves_classe'
    ),

    # ========================================================
    # MATIERES ENSEIGNEES DANS UNE CLASSE
    # ========================================================

    path(
        'enseignants/<int:id_enseignant>/classes/<int:id_classe>/matieres/',
        MatieresClasseEnseignantAPIView.as_view(),
        name='matieres_classe'
    ),

    # ========================================================
    # NOTES
    # ========================================================

    path(
        'enseignants/<int:id_enseignant>/eleves/<int:id_eleve>/notes/',
        NotesEleveAPIView.as_view(),
        name='notes_eleve'
    ),

    path(
        'enseignants/<int:id_enseignant>/notes/<int:id_note>/',
        NoteDetailAPIView.as_view(),
        name='note_detail'
    ),

    # ========================================================
    # ABSENCES
    # ========================================================

    path(
        'enseignants/<int:id_enseignant>/eleves/<int:id_eleve>/absences/',
        AbsencesEleveAPIView.as_view(),
        name='absences_eleve'
    ),

    path(
        'enseignants/<int:id_enseignant>/absences/<int:id_absence>/',
        AbsenceDetailAPIView.as_view(),
        name='absence_detail'
    ),

    # ========================================================
    # REMARQUES
    # ========================================================

    path(
        'enseignants/<int:id_enseignant>/eleves/<int:id_eleve>/remarques/',
        RemarquesEleveAPIView.as_view(),
        name='remarques_eleve'
    ),

    path(
        'enseignants/<int:id_enseignant>/remarques/<int:id_remarque>/',
        RemarqueDetailAPIView.as_view(),
        name='remarque_detail'
    ),

    # ========================================================
    # SANCTIONS
    # ========================================================

    path(
        'enseignants/<int:id_enseignant>/eleves/<int:id_eleve>/sanctions/',
        SanctionsEleveAPIView.as_view(),
        name='sanctions_eleve'
    ),

    path(
        'enseignants/<int:id_enseignant>/sanctions/<int:id_sanction>/',
        SanctionDetailAPIView.as_view(),
        name='sanction_detail'
    ),

    # ========================================================
    # BULLETINS
    # ========================================================

    path(
        'enseignants/<int:id_enseignant>/eleves/<int:id_eleve>/bulletins/',
        BulletinsEleveAPIView.as_view(),
        name='bulletins_eleve'
    ),

    path(   
        'enseignants/<int:id_enseignant>/bulletins/<int:id_bulletin>/',
        BulletinDetailAPIView.as_view(),
        name='bulletin_detail'
    ),
]

