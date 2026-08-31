# from django.shortcuts import render

# # Create your views here.

# def pageparent(request):
#     return render(request,'parent/parent.html')






from django.shortcuts import render

def pageparent(request):
    return render(request, 'parent/pageparent.html')

def monenfant(request):
    return render(request, 'parent/monenfant.html')

def mesnotes(request):
    return render(request, 'parent/mesnotes.html')

def leparametre(request):
    return render(request, 'parent/leparametre.html')

def madiscipline(request):
    return render(request, 'parent/madiscipline.html')

def mesnotifications(request):
    return render(request, 'parent/mesnotifications.html')