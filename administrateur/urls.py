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
        path('inscription/',views.inscription,name='inscription')
]