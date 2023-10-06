import uuid

from django.db import models


class RateTable(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    fee_rate = models.FloatField()
    partner_comission = models.FloatField()

    class Meta:
        ordering = ["name"]

    def __repr__(self) -> str:
        return f"Rate Table Name: {self.name} / PK: {self.pk}"
