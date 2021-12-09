import json
from django.core import serializers
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import json 
from django.contrib import messages

from .models import*
def index(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return checker(request,user,user.pk)
        else:
            messages.error(request,'Введен неверный логин или пароль')
            return render(request,'app1/signin.html')
    else:
        return render(request,'app1/signin.html')

@login_required(login_url='')
def checker(request,user,assetid):

    devices=serializers.serialize("json",App1.objects.filter(user=assetid))
    devices2=serializers.serialize("json",Devices.objects.filter(messages_id=1))
    messages=serializers.serialize("json",Messages.objects.filter(id=1))
    print(devices2)
    print(messages)
    context={
        "animals" : devices,
    }

    if user is not None:
        return render(request,'app1/map.html', context=context,)


def pageNotFound(request,exception):
    return HttpResponseNotFound('NOT FOUND 404')




