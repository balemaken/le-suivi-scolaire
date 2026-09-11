# from django.shortcuts import render

# # Create your views here.

# def pageteach(request):
#     return render(request,'teacher/teacher.html')






from django.shortcuts import render
from user.decorators import login_required_by_role


@login_required_by_role('enseignant')
def pageteacher(request):
    return render(request, 'teacher/pageteacher.html')



@login_required_by_role('enseignant')
def élève(request):
    return render(request,'teacher/élève.html') 



@login_required_by_role('enseignant')
def messages(request):
    return render(request,'teacher/messages.html') 



@login_required_by_role('enseignant')
def emploi(request):
    return render(request,'teacher/emploi.html') 



@login_required_by_role('enseignant')
def notes(request):
    return render(request,'teacher/notes.html') 




@login_required_by_role('enseignant')
def parametre(request):
    return render(request,'teacher/parametre.html') 



@login_required_by_role('enseignant')
def classes(request):
    return render(request,'teacher/classes.html') 




@login_required_by_role('enseignant')
def inscriptionEnseignant(request):
    return render(request,'teacher/inscription.html')







@login_required_by_role('enseignant')
def absences(request):
    return render(request,'teacher/absences.html') 






@login_required_by_role('enseignant')
def remarques(request):
    return render(request,'teacher/remarques.html')





@login_required_by_role('enseignant')
def sanctions(request):
    return render(request,'teacher/sanctions.html') 





@login_required_by_role('enseignant')
def bulletins(request):
    return render(request, 'teacher/bulletins.html')
