import uuid

from django.db import models


class RateTable(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)

    solicitation = models.OneToOneField(
        "solicitation.Solicitation", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["name"]

    def __repr__(self) -> str:
        return f"Table Name: {self.name} / PK: {self.pk}"
