from django.urls import path

from .views import*

urlpatterns=[
    path('',index,name='main page'),
    # path('device/<int:assetid>/',checker)
]