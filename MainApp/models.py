from django.db import models


# Create your models here.
class Languages(models.Model):
    name = models.CharField(max_length=50)


class Country(models.Model):
    name = models.CharField(max_length=100)
