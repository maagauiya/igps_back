from django.urls import path

from .views import*

urlpatterns=[
    path('',index,name='main page'),
    path('map/<int:assetid>',checker,name='map')
    # path('device/<int:assetid>/',checker)
]