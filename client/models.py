import uuid

from django.db import models


class Client(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)

    bank = models.OneToOneField("bank.Bank", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __repr__(self) -> str:
        return f"Client Name: {self.name} / PK: {self.pk}"
