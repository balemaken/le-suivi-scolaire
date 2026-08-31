from django.urls import path
from . import views

urlpatterns = [
    path('dashboarparent/',views.pageparent, name='pageparent'),
      path('monenfant/',views.monenfant, name='monenfant'),
      path('nmesotes/',views.mesnotes, name='mesnotes'),
      path('madiscipline/',views.madiscipline, name='madiscipline'),
      path('mesnotifications/',views.mesnotifications, name='mesnotifications'),
      path('leparametre/',views.leparametre, name='leparametre')
]