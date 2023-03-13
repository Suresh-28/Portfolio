from django.db import models


class Candidshoot(models.Model):

    img = models.ImageField(upload_to='pics1')