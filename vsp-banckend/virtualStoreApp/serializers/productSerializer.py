from virtualStoreApp.models.order import Order
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'idProvider', 'name', 'units', 'price']
