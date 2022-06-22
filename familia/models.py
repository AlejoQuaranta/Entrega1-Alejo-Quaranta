from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    relationship = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    cellphone = models.IntegerField(unique=True)


