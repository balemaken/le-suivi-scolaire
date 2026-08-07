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

def discipline(request):
    return render(request,'administrateur/discipline.html') 