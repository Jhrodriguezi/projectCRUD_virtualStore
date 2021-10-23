from virtualStoreApp.models.user import User
from virtualStoreApp.models.order import Order
from rest_framework import serializers
from .orderSerializer import OrderSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'name', 'lastname', 'email')

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, instance):
        user = User.objects.get(id=instance.id)
        return {
            "id": user.id,
            "username": user.username,
            "name": user.name,
            "lastname":user.lastname,
            "email": user.email,
        }
