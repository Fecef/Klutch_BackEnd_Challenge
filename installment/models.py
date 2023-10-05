import uuid

from django.db import models


class Installment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    installments = models.PositiveSmallIntegerField()
    installments_interest = models.DecimalField(max_digits=12, decimal_places=2)
    installment_value = models.DecimalField(max_digits=12, decimal_places=2)
    full_value = models.DecimalField(max_digits=12, decimal_places=2)
    comission = models.DecimalField(max_digits=12, decimal_places=2)

    rate_table = models.ForeignKey(
        "rate_table.RateTable", on_delete=models.CASCADE, related_name="installments"
    )

    class Meta:
        ordering = ["installment_value"]

    def __repr__(self) -> str:
        return f"Installment Value: {self.installment_value} / PK: {self.pk}"
