from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

from .models import*
# Create your views here.

def index(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return checker(request,user,user.pk)
        else:
            return HttpResponse('unsucc')
    else:
        return render(request,'app1/signin.html')
@csrf_protect
def checker(request,user,assetid):
    devices=App1.objects.filter(user=assetid)
    context={
        'animals':devices,
    }
    if user is not None:
        return render(request,'app1/test.html',context=context)
    else:
        return HttpResponse('unsucc')


def pageNotFound(request,exception):
    return HttpResponseNotFound('NOT FOUND 404')




