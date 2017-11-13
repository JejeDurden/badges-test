from django.db import models
from django.contrib.auth.models import User


class Star(models.Model):
    user = models.OneToOneField(User, primary_key=True)


class Collector(models.Model):
    user = models.OneToOneField(User, primary_key=True)


class Pioneer(models.Model):
    user = models.OneToOneField(User, primary_key=True)
