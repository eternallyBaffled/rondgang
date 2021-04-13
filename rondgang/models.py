from datetime import date
from django.db import models

# Create your models here.
class Gemeente(models.Model):
    naam_text = models.CharField(max_length=50)
    deelgemeente_text = models.CharField(max_length=50)


class Segment(models.Model):
    gemeente = models.CharField(max_length=55)
    straat = models.CharField(max_length=50)
    commentaar = models.TextField()


class Status(models.Model):
    gemeente = models.CharField(max_length=20)
    straat = models.CharField(max_length=50)
    afgewerkt = models.BooleanField()
    lid = models.CharField(max_length=50)
    datum = models.DateField(default=date.today)
    commentaar = models.TextField()
