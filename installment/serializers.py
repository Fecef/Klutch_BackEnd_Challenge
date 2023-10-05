from rest_framework import serializers

from .models import Installment


class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = [
            "id",
            "installments",
            "installments_interest",
            "installment_value",
            "full_value",
            "comission",
        ]
