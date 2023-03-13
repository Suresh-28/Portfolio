from django.db import models

class Childshoot(models.Model):
    img = models.ImageField(upload_to='pics') 

