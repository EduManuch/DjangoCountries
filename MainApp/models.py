from django.db import models


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"Language <{self.name}>"


class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Language)

    def __repr__(self):
        return f"Country <{self.name}>"
