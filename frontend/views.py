from django.shortcuts import render

# Create your views here.

def pageAcceuil(request):
    return render(request,'frontend/pageAcceuil.html')

def login(request):
    return render(request,'frontend/login.html')

def inscription(request):
    return render(request,'frontend/inscription.html')

def apropos(request):
    return render(request,'frontend/apropos.html')   

def contacte(request):
    return render(request,'frontend/contacte.html') 

