from django.db import models

class Weedshoot(models.Model):
    img = models.ImageField(upload_to='pics') 

