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
    
