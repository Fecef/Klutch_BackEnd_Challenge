import uuid

from django.db import models


class Solicitation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    installmentInterest = models.DecimalField(max_digits=12, decimal_places=2)
    installmentInterestValue = models.DecimalField(max_digits=12, decimal_places=2)
    comission = models.DecimalField(max_digits=12, decimal_places=2)
    comissionValue = models.DecimalField(max_digits=12, decimal_places=2)
    installmentValue = models.DecimalField(max_digits=12, decimal_places=2)
    cardNumber = models.CharField(max_length=20)
    desiredValue = models.DecimalField(max_digits=12, decimal_places=2)
    totalLoan = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        ordering = ["totalLoan"]

    def __repr__(self) -> str:
        return f"Solicitation Loan: {self.totalLoan} / PK: {self.pk}"
