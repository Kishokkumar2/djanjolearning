from django.db import models

class Room(models.Model):
   
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)