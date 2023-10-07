from rest_framework import serializers
from datetime import datetime
from .models import Solicitation


class SolicitationSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Solicitation
        fields = [
            "id",
            "installments",
            "installment_value",
            "loan_to_get",
            "loan_to_pay",
            "modality",
            "stream",
            "client",
            "rate_table",
            "created_at",
            "updated_at",
        ]

    def get_created_at(self, obj: Solicitation):
        now = datetime.now()
        obj.created_at = now.strftime("%Y-%m-%d %H:%M:%S")

        return obj.created_at

    def get_updated_at(self, obj: Solicitation):
        now = datetime.now()
        obj.updated_at = now.strftime("%Y-%m-%d %H:%M:%S")

        return obj.updated_at
