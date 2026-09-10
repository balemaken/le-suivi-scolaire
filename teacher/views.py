# from django.shortcuts import render

# # Create your views here.

# def pageteach(request):
#     return render(request,'teacher/teacher.html')






from django.shortcuts import render

def pageteacher(request):
    return render(request, 'teacher/pageteacher.html')

def élève(request):
    return render(request,'teacher/élève.html') 

def messages(request):
    return render(request,'teacher/messages.html') 

def emploi(request):
    return render(request,'teacher/emploi.html') 

def notes(request):
    return render(request,'teacher/notes.html') 


def parametre(request):
    return render(request,'teacher/parametre.html') 

def classes(request):
    return render(request,'teacher/classes.html') 

def inscriptionEnseignant(request):
    return render(request,'teacher/inscription.html')


def absences(request):
    return render(request,'teacher/absences.html') 


def remarques(request):
    return render(request,'teacher/remarques.html')


def sanctions(request):
    return render(request,'teacher/sanctions.html') 

def bulletins(request):
    return render(request, 'teacher/bulletins.html')
