from rest_framework import serializers

from bank.serializers import BankSerializer
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    bank = BankSerializer()

    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "phone",
            "cpf",
            "bank",
        ]
        depth = 1

    def create(self, validated_data):
        bank_data = validated_data.pop("bank")
        bank_serializer = BankSerializer(data=bank_data)
        bank_serializer.is_valid(raise_exception=True)
        bank = bank_serializer.save()

        client = Client.objects.create(**validated_data, bank=bank)
        return client
