from django.db import models


class Eventshoot(models.Model):

    img = models.ImageField(upload_to='pics1')