import json
from django.core import serializers
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
import json 
from django.contrib import messages
from pymongo import MongoClient
from pprint import pp, pprint
from django.contrib.auth.models import User
from pymongo import MongoClient
from django.contrib.auth import get_user_model 
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
    


        
    # with open("/Users/maagauiya/Desktop/self_study/djangoo — копия/testsite/app1/asset.json") as jsonFile:
    #     jsonObject = json.load(jsonFile)
    #     for i in range(len(jsonObject)):
    #         print(i)
    #         assetss=App1()
    #         assetss.id=i
    #         assetss.user=jsonObject[i]['user']
    #         assetss.device=jsonObject[i]['device']
    #         assetss.asset_name=jsonObject[i]['asset_name']
    #         assetss.current_lat=jsonObject[i]['current_lat']
    #         assetss.current_lng=jsonObject[i]['current_lng']
    #         assetss.battery_status=jsonObject[i]['battery_status']
    #         assetss.is_inzone=jsonObject[i]['is_inzone']
    #         assetss.datetime=jsonObject[i]['datetime']
    #         assetss.save()










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

    client=MongoClient("mongodb+srv://maagauiya:loopcool@cluster0.f7uie.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["igpstest"]
    collection = db["app1_app1"]
    userr=0

    # cursor=collection.find({ "user": { "$exists": "true" },"id":assetid })
    # for doc in cursor:
    #     userr=doc["user"]
    collection = db["device"]
    esn=[]
    # print(assetid)
    # print(userr)
    cursor=collection.find({ "messenger_id": { "$exists": "true" },"user":assetid })
    for doc in cursor:
        esn.append(doc["messenger_id"])

    print(esn)
    collection = db["devices"]
    messages=[]
    for i in range(len(esn)):
        cursor=collection.find({ "messages": { "$exists": "true" },"esn":esn[i] })
        for doc in cursor:
            messages.append(doc["messages"])

    #pprint(messages)
    coordinates = []
    for i in range(len(messages)):
        num = len(messages[i])
        coordinates.append([{'lat':decodeStPayLat(messages[i][k]["payload"]),'lng':decodeStPayLng(messages[i][k]["payload"])} for k in range(num-11, num - 1)])
    devices=serializers.serialize("json",App1.objects.filter(user=int(assetid)))
    
    context={
        "animals" : devices,
        "coordinates" : coordinates
    }
    # print(coordinates)
    if user is not None:
        return render(request,'app1/map.html', context=context,)


def pageNotFound(request,exception):
    return HttpResponseNotFound('NOT FOUND 404')




