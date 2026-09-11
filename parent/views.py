# from django.shortcuts import render

# # Create your views here.

# def pageparent(request):
#     return render(request,'parent/parent.html')






from django.shortcuts import render


from user.decorators import login_required_by_role





@login_required_by_role('parent')
def pageparent(request):
    return render(request, 'parent/pageparent.html')





@login_required_by_role('parent')
def monenfant(request):
    return render(request, 'parent/monenfant.html')





@login_required_by_role('parent')
def mesnotes(request):
    return render(request, 'parent/mesnotes.html')




@login_required_by_role('parent')
def leparametre(request):
    return render(request, 'parent/leparametre.html')




@login_required_by_role('parent')
def madiscipline(request):
    return render(request, 'parent/madiscipline.html')






@login_required_by_role('parent')
def mesnotifications(request):
    return render(request, 'parent/mesnotifications.html')



@login_required_by_role('parent')
def remarques(request):
    return render(request, 'parent/mesremarques.html')






@login_required_by_role('parent')
def sanctions(request):
    return render(request,'parent/messanctions.html')




@login_required_by_role('parent')
def bulletins(request):
    return render(request,'parent/mesbulletins.html')





@login_required_by_role('parent')
def ia(request):
    return render (request,'parent/ia_schoolconnect.html')




