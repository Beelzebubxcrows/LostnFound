from django.db import models




class Lost(models.Model):
    hostel= models.CharField(max_length=15, blank=False)
    name=  models.CharField(max_length=15, blank=False)
    room=  models.IntegerField(blank=False)
    thing= models.CharField(max_length=15, blank=False)
    description =  models.CharField(max_length=50, blank=False)

class Found(models.Model):
    Name=models.CharField(max_length=15, blank=False)
    Place=models.CharField(max_length=15, blank=False)
    Thing=models.CharField(max_length=15, blank=False)
    Description=models.CharField(max_length=30, blank=False)

    
    
    
