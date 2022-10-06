from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20, null=True)
    summary = models.CharField(max_length=500, null=True)
    weight = models.IntegerField(default=0, null=True)
    part = models.CharField(max_length=20, null=True)
    active = models.CharField(max_length=50, null=True)
