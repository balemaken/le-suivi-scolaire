from django.urls import path
from . import views

urlpatterns = [
    path('dashboarparent/',views.pageparent, name='pageparent')
]