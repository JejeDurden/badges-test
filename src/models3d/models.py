from django.db import models
from django.contrib.auth.models import User


class Model(models.Model):
    name = models.CharField(max_length=48)
    file = models.FileField(upload_to='uploads/', max_length=256)
    user = models.ForeignKey(User, related_name='models')
    vertice_count = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
