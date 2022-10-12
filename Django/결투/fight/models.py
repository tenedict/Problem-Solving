from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20,null=True)
    gs1 = models.IntegerField(default=0,null=True)
    gs2 = models.IntegerField(default=0,null=True)
    gs3 = models.IntegerField(default=0,null=True)
    gs4 = models.IntegerField(default=0,null=True)
    attack = models.IntegerField(default=10,null=True)
    defense = models.IntegerField(default=10,null=True)
    types = models.CharField(max_length=20,null=True)