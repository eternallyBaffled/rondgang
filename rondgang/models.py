from datetime import date
from django.db import models

# Create your models here.
class Gemeente(models.Model):
    naam_text = models.CharField(max_length=50)
    deelgemeente_text = models.CharField(max_length=50)


class Segment(models.Model):
    gemeente = models.CharField(max_length=55)
    straat = models.CharField(max_length=50)
    commentaar = models.TextField(blank=True)

    def __str__(self):
        return '%s, %s' % (self.straat, self.gemeente)

    class Meta:
        verbose_name_plural = 'segmenten'


class Status(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    afgewerkt = models.BooleanField()
#    lid = models.ForeignKey(Lid, to_field='naam')
    lid = models.CharField(max_length=50, null=True)
    datum = models.DateField(default=date.today)
    commentaar = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'statussen'
