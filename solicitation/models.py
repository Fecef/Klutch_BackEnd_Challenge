import uuid

from django.db import models


class Solicitation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    installments = models.PositiveSmallIntegerField()
    installment_value = models.DecimalField(max_digits=12, decimal_places=2)
    loan_to_get = models.DecimalField(max_digits=12, decimal_places=2)
    loan_to_pay = models.DecimalField(max_digits=12, decimal_places=2)

    client = models.OneToOneField("client.Client", on_delete=models.CASCADE)
    rate_table = models.OneToOneField("rate_table.RateTable", on_delete=models.CASCADE)

    class Meta:
        ordering = ["loan_to_get"]

    def __repr__(self) -> str:
        return f"Solicitation Loan: {self.loan_to_get} / PK: {self.pk}"
