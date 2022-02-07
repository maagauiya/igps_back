from django.urls import path

from .views import*

urlpatterns=[
    path('',index,name='main page'),
    path('map/<int:assetid>',checker,name='map'),
    path('manage/',manage,name='manage')
    # path('device/<int:assetid>/',checker)
]