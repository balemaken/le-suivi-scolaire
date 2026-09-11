# from django.shortcuts import render

# # Create your views here.

# def pageadmin(request):
#     return render(request,'administrateur/administrateur.html')






from django.shortcuts import render
from user.decorators import login_required_by_role


@login_required_by_role('admin')
def pageadmin(request):
    return render(request, 'administrateur/pageadmin.html')


@login_required_by_role('admin')
def élève(request):
    return render(request,'administrateur/élève.html') 


@login_required_by_role('admin')
def message(request):
    return render(request,'administrateur/message.html') 



@login_required_by_role('admin')
def enseignant(request):
    return render(request,'administrateur/enseignant.html') 


@login_required_by_role('admin')
def notesBulletin(request):
    return render(request,'administrateur/notesBulletin.html') 

@login_required_by_role('admin')
def parametre(request):
    return render(request,'administrateur/parametre.html') 


# @login_required_by_role('admin')
def inscriptionAdmin(request):
    return render(request,'administrateur/inscription.html') 



@login_required_by_role('admin')
def discipline(request):
    return render(request,'administrateur/discipline.html') 



@login_required_by_role('admin')
def dashboard_admin(request):
    return render(request, 'administrateur/dashboard_admin.html')


@login_required_by_role('admin')
def classes_admin(request):
    return render(request, 'administrateur/classes_admin.html')



@login_required_by_role('admin')
def matieres_admin(request):
    return render(request, 'administrateur/matieres_admin.html')



@login_required_by_role('admin')
def eleves_admin(request):
    return render(request, 'administrateur/eleves_admin.html')




@login_required_by_role('admin')
def enseignants_admin(request):
    return render(request, 'administrateur/enseignants_admin.html')



@login_required_by_role('admin')
def parents_admin(request):
    return render(request, 'administrateur/parents_admin.html')


@login_required_by_role('admin')
def liaisons_admin(request):
    return render(request, 'administrateur/liaisons_admin.html')



@login_required_by_role('admin')
def affectations_admin(request):
    return render(request, 'administrateur/affectations_admin.html')



@login_required_by_role('admin')
def parametres_admin(request):
    return render(request, 'administrateur/parametres_admin.html')
