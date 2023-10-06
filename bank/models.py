import uuid

from django.db import models


class Bank(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    agency = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __repr__(self) -> str:
        return f"Bank Name: {self.name} / PK: {self.pk}"
