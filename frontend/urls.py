from django.urls import path
from . import views

urlpatterns = [
    path('', views.pageAcceuil, name='pageAcceuil'),
    path('login/', views.login, name='login'),
    path('incription/',views.inscription,name='inscription'),
    path('apropos/',views.apropos,name='apropos')
]