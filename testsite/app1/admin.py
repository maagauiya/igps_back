from django.contrib import admin
from .models import*
from pymongo import MongoClient
from sshtunnel import SSHTunnelForwarder
import pandas as pd
from django.contrib import admin
from django_object_actions import DjangoObjectActions
from django.contrib.auth.models import User
from .Google import Create_Service # download source from the link in the description
import pandas as pd
import os
from .Google import Create_Service
from multiprocessing.dummy import current_process
from sqlite3 import Cursor
import pandas as pd
from sshtunnel import SSHTunnelForwarder
from pymongo import MongoClient

# class ImportAdmin(DjangoObjectActions, admin.ModelAdmin):
#     def Update(modeladmin, request, queryset):
#         print(1)
#         CLIENT_SECRET_FILE = '/Users/maagauiya/Desktop/self_study/djangoo — копия/testsite/app1/static/app1/client_secret.json'
#         API_SERVICE_NAME = 'sheets'
#         API_VERSION = 'v4'
#         SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#         GOOGLE_SHEET_ID = '1Cb7iwhw5ov1MtYnyLA6Mgkx_NjEUSuu1_dkvzlBgj7Q'
#         print(2)
#         service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
#         print(3)

#         """
#         Iterate Worksheets
#         """
#         client=MongoClient("mongodb+srv://maagauiya:loopcool@cluster0.f7uie.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#         db = client["igpstest"]
#         collection=db['lastnumber']
#         last=None
#         cursor=collection.find()
#         for i in cursor:
#             last=i['last']
#         gsheets = service.spreadsheets().get(spreadsheetId=GOOGLE_SHEET_ID).execute()
#         sheets = gsheets['sheets']
#         for sheet in sheets:
#             if sheet['properties']['title'] != 'master':
#                 dataset = service.spreadsheets().values().get(
#                     spreadsheetId=GOOGLE_SHEET_ID,
#                     range=sheet['properties']['title'],
#                     majorDimension='ROWS'
#                 ).execute()
#                 df = pd.DataFrame(dataset['values'])
#                 df.columns = df.iloc[0]
#                 df.drop(df.index[0], inplace=True)
#                 df.to_csv(sheet['properties']['title'] + '.csv', index=False)
#         MONGO_HOST = "46.101.236.239"
#         MONGO_DB = "sttechdb"
#         MONGO_USER = "bekald"
#         MONGO_PASS = "dndrBPVmTRr8"

#         server = SSHTunnelForwarder(
#             (MONGO_HOST, 1220),
#             ssh_username=MONGO_USER,
#             ssh_password=MONGO_PASS,
#             remote_bind_address=('127.0.0.1', 27017)
#             )

#         server.start()

#         client2 = MongoClient('127.0.0.1', server.local_bind_port)
#         db2 = client2[MONGO_DB]
#         client=MongoClient("mongodb+srv://maagauiya:loopcool@cluster0.f7uie.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


#         fields = ['Login','Password','Name','Email']
#         db = client["igpstest"]
#         df = pd.read_csv('/Users/maagauiya/Desktop/self_study/djangoo — копия/testsite/Spot Trace.csv', skipinitialspace=True, usecols=fields)
#         for i in range(last,len(df)):
#             # print(i)
#             collection = db2["latest_spot_messages"]
#             messengerId=''
        
#             cursor=collection.find({ "messengerId": { "$exists": "true" },"username":df.Login[i]})
#             state=False
#             for doc1 in cursor:
#                 if state==True:
#                     break
            
#                 print(i," ",df.Login[i]," ",df.Password[i])
#                 collection = db2["device"]
#                 cursor=collection.find({ "user": { "$exists": "true" },"messenger_id":doc1['messengerId']})
#                 for doc in cursor:
#                     user = User.objects.create_user(
#                                         id=doc['user'],
#                                         username=df.Login[i],
#                                         #  email=df.Email[i],
#                                         password=df.Password[i],
#                                         is_superuser=False,
#                                         first_name=str(df.Name[i]),
#                                         )

#                     user.save()
#                     print(doc['user'])
#                     state=True
#                     break
#             collection=db['lastnumber']
#             myquery = { "last": last }
#             newvalues = { "$set": { "last": len(df)-1 } }
#             collection.update_one(myquery, newvalues)
    
#     changelist_actions = ('Update', )
# # class UserAdmin(admin.ModelAdmin):
# #     def save_model(self, request, obj, form, change):
# #         obj.user = request.user
# #         print(obj.password)
# #         super().save_model(request, obj, form, change)
# # admin.site.unregister(User)
# # admin.site.register(User)
admin.site.register(App1)
admin.site.register(Devices)
admin.site.register(Messages)











