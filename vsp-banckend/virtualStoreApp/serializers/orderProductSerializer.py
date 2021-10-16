from virtualStoreApp.models.order import Order
from rest_framework import serializers


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'idOrder', 'idProduct', 'products']
