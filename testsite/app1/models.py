from django.db import models


class App1(models.Model):
    user=models.IntegerField(blank=True,null=True)
    device=models.IntegerField(blank=True,null=True)
    asset_name=models.CharField(max_length=100,blank=True,null=True)
    current_lat=models.FloatField(blank=True,null=True)
    current_lng=models.FloatField(blank=True,null=True)
    battery_status=models.CharField(max_length=15,blank=True,null=True)
    is_inzone=models.BooleanField(blank=True,null=True)
    datetime=models.DateTimeField(blank=True,null=True)

class Devices(models.Model):
    esn = models.CharField(max_length=10,blank=True,null=True)
    username = models.CharField(max_length=100,blank=True,null=True)
    messages=models.ForeignKey('Messages', related_name='messages', on_delete=models.CASCADE,null=True)


class Messages(models.Model):
    timeStamp = models.DateTimeField()
    messageID = models.CharField(max_length=50,blank=True,null=True)
    esn = models.CharField(max_length=10,blank=True,null=True)
    unixTime = models.CharField(max_length=10,blank=True,null=True)
    gps = models.CharField(max_length=10,blank=True,null=True)
    payload = models.CharField(max_length=30,blank=True,null=True)