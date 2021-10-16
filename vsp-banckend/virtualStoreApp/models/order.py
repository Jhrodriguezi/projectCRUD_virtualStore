from django.db import models
from .user import User

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.CharField(max_length=50)
    products = models.SmallIntegerField()
    