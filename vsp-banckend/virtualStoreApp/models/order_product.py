from django.db import models
from .order import Order
from .product import Product


class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True)
    idOrder = models.ForeignKey(
        Order, related_name="Order", on_delete=models.CASCADE)
    idProduct = models.ForeignKey(
        Product, related_name="Product", on_delete=models.CASCADE)
    products = models.SmallIntegerField()
