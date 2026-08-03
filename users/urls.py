from django.urls import path

from .views import *


urlpatterns=[

  path("register/parent/",ParentRegisterView.as_view()),

    path("register/enseignant/",EnseignantRegisterView.as_view()),

    path("register/admin/",AdminRegisterView.as_view()),


    path( "login/",LoginView.as_view()),

]