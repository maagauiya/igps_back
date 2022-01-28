import json
from django.core import serializers
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import json 
from django.contrib import messages
from django.contrib.auth.models import User
from pymongo import MongoClient
from sshtunnel import SSHTunnelForwarder
from bson.json_util import dumps, loads
import pandas as pd
import time

from .models import*
def index(request):
    
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('map/{}'.format(user.pk))
        else:
            messages.error(request,'Введен неверный логин или пароль')
            return render(request,'app1/signin.html')
    else:
        return render(request,'app1/signin.html')

@login_required(login_url='')
def checker(request,assetid,*args, **kwargs):
     

    if assetid != request.user.id:
        return redirect('/map/{}'.format(request.user.id))
    

    if request.POST.get('logout'):
        logout(request)
        return redirect('/')

    def decodeStPayLat(strp):
        lat = strp[4:10]
        ilat=int(lat,16)
        latt = ilat * (90.0/2**23)
        return latt

    def decodeStPayLng(strp):
        logt = strp[10:16]
        ilogt=int(logt,16)
        longtt = ilogt * (180.0/2**23)
        lngtt=0.0
        if (longtt > 180):
            lngtt = longtt - 360
        else:
            lngtt = -longtt
        return -lngtt

    MONGO_HOST = "46.101.236.239"
    MONGO_DB = "sttechdb"
    MONGO_USER = "bekald"
    MONGO_PASS = "dndrBPVmTRr8"

    server = SSHTunnelForwarder(
        (MONGO_HOST, 1220),
        ssh_username=MONGO_USER,
        ssh_password=MONGO_PASS,
        remote_bind_address=('127.0.0.1', 27017)
    )

    server.start()

    client2 = MongoClient('127.0.0.1', server.local_bind_port)
    db2 = client2[MONGO_DB]
    #collection = db2[]

        # print(assetid)
        # print(userr)
    
    

    

    # client=MongoClient("mongodb+srv://maagauiya:loopcool@cluster0.f7uie.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # db = client["igpstest"]
    collection = db2["asset"]
    userr=0
    
    cursor=collection.find({ "user": assetid,"id": { "$exists": "true" }})
    
    for doc in cursor:
        userr=doc["id"]

    collection = db2["device"]
    esn=[]
    cursor=collection.find({ "messenger_id": { "$exists": "true" },"user":assetid })
    for doc in cursor:
        esn.append(doc["messenger_id"])


    collection = db2["devices"]
    messages=[]
    for i in range(len(esn)):
        cursor=collection.find({ "messages": { "$exists": "true" },"esn":esn[i] })
        for doc in cursor:
            messages.append(doc["messages"])
    
    coordinates = []
 
    for i in range(len(messages)):
        num = len(messages[i])
        if(num>=10):
            coordinates.append([{'lat':decodeStPayLat(messages[i][k]["payload"]),'lng':decodeStPayLng(messages[i][k]["payload"])} for k in range(num-11, num - 1)])
        else:
            coordinates.append([{'lat':decodeStPayLat(messages[i][k]["payload"]),'lng':decodeStPayLng(messages[i][k]["payload"])} for k in range(0, num)])

    
    # devices=serializers.serialize("json",App1.objects.filter(user=assetid))
    # context={
    #     "animals" : devices,
    #     "coordinates" : coordinates
    # }
    # print(type(devices))


    collection=db2["asset"]
    cursor = collection.find(({ "user": assetid}))
    cursor = dumps(cursor)
    print(cursor)
    print(type(cursor))
    context={
        "animals" : cursor,
        "coordinates" : coordinates
    }


    server.stop()
    return render(request,'app1/map.html', context=context,)


    



def pageNotFound(request,exception):
    context = {}
    response = render(request, "app1/error.html", context=context)
    response.status_code = 404
    return response








































