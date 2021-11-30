import json
from django.core import serializers
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import json 
from django.forms.models import model_to_dict

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

@login_required(login_url='')
def checker(request,user,assetid):
    devices=App1.objects.filter(user=assetid)
    context={
        "animals" : devices,
    }
    # devices2=serializers.serialize("json",context)
    
    # print(devices2)

    # devices=serializers.serialize("json",App1.objects.filter(user=assetid))
    # print(devices)
    if user is not None:
        #return render(request,'app1/map.html', context = json.dumps(context.dict))
        return render(request,'app1/map.html', context=context)


def pageNotFound(request,exception):
    return HttpResponseNotFound('NOT FOUND 404')




