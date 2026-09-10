# from django.shortcuts import render

# # Create your views here.

# def pageadmin(request):
#     return render(request,'administrateur/administrateur.html')






from django.shortcuts import render

def pageadmin(request):
    return render(request, 'administrateur/pageadmin.html')

def élève(request):
    return render(request,'administrateur/élève.html') 

def message(request):
    return render(request,'administrateur/message.html') 

def enseignant(request):
    return render(request,'administrateur/enseignant.html') 

def notesBulletin(request):
    return render(request,'administrateur/notesBulletin.html') 


def parametre(request):
    return render(request,'administrateur/parametre.html') 

def inscriptionAdmin(request):
    return render(request,'administrateur/inscription.html') 

def discipline(request):
    return render(request,'administrateur/discipline.html') 




def dashboard_admin(request):
    return render(request, 'administrateur/dashboard_admin.html')

def classes_admin(request):
    return render(request, 'administrateur/classes_admin.html')

def matieres_admin(request):
    return render(request, 'administrateur/matieres_admin.html')

def eleves_admin(request):
    return render(request, 'administrateur/eleves_admin.html')

def enseignants_admin(request):
    return render(request, 'administrateur/enseignants_admin.html')

def parents_admin(request):
    return render(request, 'administrateur/parents_admin.html')

def liaisons_admin(request):
    return render(request, 'administrateur/liaisons_admin.html')

def affectations_admin(request):
    return render(request, 'administrateur/affectations_admin.html')

def parametres_admin(request):
    return render(request, 'administrateur/parametres_admin.html')
