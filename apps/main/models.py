from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#user
#band
#event
#establishment

class Band(models.Model):
    web_link = models.URLField(max_length=255)
    playlist = models.URLField(max_length=300)
    contacte_email = models.CharField(max_length=100)
    contacte_mobil = models.CharField(max_length=16) 
    image = models.ImageField(upload_to = 'img/', default = '') 
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='band')

class Event(models.Model):
    STATE = [
        ("SR", "Searching"),
        ("CL", "Closed"),
        ("FN", "Finalized")
    ]
    band = models.ManyToManyField('Band', related_name='events')
    state = models.CharField(max_length=2, choices=STATE, default="SR") 
    date = models.DateTimeField(null=False) 
    description = models.TextField()
    establishment = models.ForeignKey('Establishment', on_delete=models.CASCADE, null=False, related_name='events')    
    

class Establishment(models.Model):
    address = models.CharField(max_length=200)
    contacte_email = models.CharField(max_length=100)
    contacte_mobil = models.CharField(max_length=16) 
    image = models.ImageField(upload_to = 'img/', default = '') 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='establishments')   

    