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
         path('inscription/',views.inscription,name='inscription')
    ]