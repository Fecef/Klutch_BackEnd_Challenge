from rest_framework import serializers

from .models import Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            "id",
            "label",
            "account_type_label",
            "account_number",
        ]
