from rest_framework import serializers

from .models import RateTable


class RateTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateTable
        fields = [
            "id",
            "name",
            "fee_rate",
            "partner_comission",
        ]
