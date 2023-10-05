from rest_framework import serializers

from installment.serializers import InstallmentSerializer
from .models import RateTable


class RateTableSerializer(serializers.ModelSerializer):
    installments = InstallmentSerializer(many=True)

    class Meta:
        model = RateTable
        fields = [
            "id",
            "name",
            "installments",
        ]
        depth = 1

    def create(self, validated_data):
        installments_data = validated_data.pop("installments")
        installment_serializer = InstallmentSerializer(data=installments_data)
        installment_serializer.is_valid(raise_exception=True)
        installments = installment_serializer.save()

        rate_table = RateTable.objects.create(
            **validated_data, installments=installments
        )
        return rate_table
