from django.db import models

# Create your models here.
class Room(models.Model):
    light=models.CharField(max_length=100)
    fan=models.CharField(max_length=100)
    tv=models.CharField(max_length=100)
    def __str__(self):
        return self.light
