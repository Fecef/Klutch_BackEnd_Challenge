from rest_framework import serializers

from .models import Solicitation


class SolicitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitation
        fields = [
            "id",
            "client",
            "installment_interest",
            "installment_interest_value",
            "comission",
            "comission_value",
            "installment_value",
            "card_number",
            "desired_value",
            "total_loan",
            "rate_table",
        ]
