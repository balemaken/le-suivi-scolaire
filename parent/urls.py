from django.urls import path
from . import views

urlpatterns = [
      path('dashboarparent/',views.pageparent, name='pageparent'),
      path('monenfant/',views.monenfant, name='monenfant'),
      path('nmesotes/',views.mesnotes, name='mesnotes'),
      path('madiscipline/',views.madiscipline, name='madiscipline'),
      path('mesnotifications/',views.mesnotifications, name='mesnotifications'),
      path('leparametre/',views.leparametre, name='leparametre'),
      path('mesremarques/',views.remarques,name='mesremarques'),
      path('messanctions/',views.sanctions,name='messanctions'),
      path('mesbulletins/',views.bulletins,name='mesbulletins'),
      path('ia/',views.ia,name='ia_schoolconnect')
]