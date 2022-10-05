from django.db import models

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField(default=-1)
    name = models.CharField(max_length=20)
    types = models.TextField(blank=False)
    