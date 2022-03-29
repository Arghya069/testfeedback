from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class LedStat(models.Model):
    device_id = models.TextField(max_length=10,primary_key=True)
    led1_status   = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    led2_status   = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    led3_status   = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    imp_1   = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    imp_2   = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    imp_3   = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    temprature    = models.FloatField(null=False,default=0.0)
    def __str__(self):
        return self.device_id


class UserDevices(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    device_id = models.ForeignKey(LedStat,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username +' : '+self.device_id.device_id
    

