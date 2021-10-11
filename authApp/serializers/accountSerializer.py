from authApp.models.account import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:  # sub-clase
        model = Account
        fields = ['balance', 'lastChangeDate', 'isActive']
