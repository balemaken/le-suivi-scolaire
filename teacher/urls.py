from django.urls import path
from . import views

urlpatterns = [
    path('pageteacher/', views.pageteacher, name='pageteacher'),
      path('élève/',views.élève,name='élève'),
        path('messages/',views.messages,name='messages'),
        path('enseignant/',views.emploi,name='emploi'),
        path('notesBulletin/',views.notes,name='notes'),
        path('parametre/',views.parametre,name='parametre'),
        path('discipline/',views.classes,name='classes'),
         path('inscriptionEnseignant/',views.inscriptionEnseignant,name='inscriptionEnseignant'),
         path('classe/',views.classes,name='classes'),
         path('absences/',views.absences,name='absences'),
         path('remarques/',views.remarques,name='remarques'),
         path('sanctions',views.sanctions,name='sanctions'),
         path('bulletins/', views.bulletins, name='bulletins'),
    ]