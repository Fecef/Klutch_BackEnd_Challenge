from rest_framework import serializers

from .models import Solicitation


class SolicitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitation
        fields = [
            "id",
            "installments",
            "installment_value",
            "loan_to_get",
            "loan_to_pay",
            "client",
            "rate_table",
        ]
