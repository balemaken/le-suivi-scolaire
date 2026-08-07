# from django.shortcuts import render

# # Create your views here.

# def pageparent(request):
#     return render(request,'parent/parent.html')






from django.shortcuts import render

def pageparent(request):
    return render(request, 'parent/pageparent.html')