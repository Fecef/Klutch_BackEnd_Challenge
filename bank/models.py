import uuid

from django.db import models


class Bank(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    label = models.CharField(max_length=50)
    account_type_label = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)

    class Meta:
        ordering = ["label"]

    def __repr__(self) -> str:
        return f"Bank Label: {self.label} / PK: {self.pk}"
