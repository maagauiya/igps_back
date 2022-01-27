from django.contrib import admin
from .models import*
from pymongo import MongoClient
from pprint import pp, pprint
from sshtunnel import SSHTunnelForwarder
import pandas as pd
from django.contrib import admin
from django_object_actions import DjangoObjectActions
class ImportAdmin(DjangoObjectActions, admin.ModelAdmin):
    def Update(modeladmin, request, queryset):
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
        st2=False
        client2 = MongoClient('127.0.0.1', server.local_bind_port)
        db2 = client2[MONGO_DB]
        fields = ['Login','Password','Name','Email']
        df = pd.read_csv('igpsi.csv', skipinitialspace=True, usecols=fields)
        for i in range(len(df)):
            collection = db2["devices"]
            esn=''
            cursor=collection.find({ "esn": { "$exists": "true" },"username":df.Login[i]})
            state=False
            for doc1 in cursor:
                if state==True:
                    break
                print(df.Login[i]," ",df.Password[i])
                collection = db2["device"]
                cursor=collection.find({ "user": { "$exists": "true" },"messenger_id":doc1['esn']})
                for doc in cursor:
                    mydict = { "id": doc['user'], "password": df.Password[i],"last_login":None,"is_superuser":False
                    ,"username":df.Login[i],"first_name":str(df.Name[i]),"last_name":" ","email":df.Email[i],"is_staff":False,"is_active":True }
                    collection = db2["auth_user"]
                    x = collection.insert_one(mydict)
                    print(i)
                    print(doc['user'])
                    state=True
                    break
    changelist_actions = ('Update', )
admin.site.register(App1,ImportAdmin)
admin.site.register(Devices)
admin.site.register(Messages)




