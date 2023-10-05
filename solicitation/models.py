import uuid

from django.db import models


class Solicitation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    installment_interest = models.DecimalField(max_digits=12, decimal_places=2)
    installment_interest_value = models.DecimalField(max_digits=12, decimal_places=2)
    comission = models.DecimalField(max_digits=12, decimal_places=2)
    comission_value = models.DecimalField(max_digits=12, decimal_places=2)
    installment_value = models.DecimalField(max_digits=12, decimal_places=2)
    card_number = models.CharField(max_length=20)
    desired_value = models.DecimalField(max_digits=12, decimal_places=2)
    total_loan = models.DecimalField(max_digits=12, decimal_places=2)

    client = models.OneToOneField("client.Client", on_delete=models.CASCADE)
    rate_table = models.OneToOneField("rate_table.RateTable", on_delete=models.CASCADE)

    class Meta:
        ordering = ["total_loan"]

    def __repr__(self) -> str:
        return f"Solicitation Loan: {self.total_loan} / PK: {self.pk}"
