from django.db import models


class Destination1(models.Model):

    img = models.ImageField(upload_to='pics1')