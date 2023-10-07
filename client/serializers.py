from datetime import datetime
from rest_framework import serializers
from bank.serializers import BankSerializer
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    bank = BankSerializer()

    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "phone",
            "cpf",
            "bank",
            "created_at",
            "updated_at",
        ]
        depth = 1

    def create(self, validated_data):
        bank_data = validated_data.pop("bank")
        bank_serializer = BankSerializer(data=bank_data)
        bank_serializer.is_valid(raise_exception=True)
        bank = bank_serializer.save()

        client = Client.objects.create(**validated_data, bank=bank)
        return client

    def get_created_at(self, obj: Client):
        now = datetime.now()
        obj.created_at = now.strftime("%Y-%m-%d %H:%M:%S")

        return obj.created_at

    def get_updated_at(self, obj: Client):
        now = datetime.now()
        obj.updated_at = now.strftime("%Y-%m-%d %H:%M:%S")

        return obj.updated_at
