from django.urls import path
from . import views

urlpatterns = [
    path('pageadministrateur/',views.pageadmin, name='pageadmin'),
    path('élève/',views.élève,name='élève'),
    path('message/',views.message,name='message'),
    path('enseignant/',views.enseignant,name='enseignant'),
    path('notesBulletin/',views.notesBulletin,name='notesBulletin'),
    path('parametre/',views.parametre,name='parametre'),
    path('discipline/',views.discipline,name='discipline'),

    path('inscriptionAdmin/',views.inscriptionAdmin,name='inscriptionAdmin'),
    path('dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('classes/', views.classes_admin, name='classes_admin'),
    path('matieres/', views.matieres_admin, name='matieres_admin'),
    path('eleves/', views.eleves_admin, name='eleves_admin'),
    path('enseignants/', views.enseignants_admin, name='enseignants_admin'),
    path('parents/', views.parents_admin, name='parents_admin'),
    path('liaisons/', views.liaisons_admin, name='liaisons_admin'),
    path('affectations/', views.affectations_admin, name='affectations_admin'),
    path('parametres/', views.parametres_admin, name='parametres_admin'),
]