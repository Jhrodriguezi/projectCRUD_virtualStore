from django.db import models
from .provider import Provider

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    idProvider = models.ForeignKey(Provider, related_name='Supply', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    units = models.IntegerField()
    price = models.CharField(max_length=50)
    