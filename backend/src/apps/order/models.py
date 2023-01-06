import uuid

from django.db import models

from apps.address.models import Address
from apps.client.models import Client


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=False, on_delete=models.CASCADE)
    order_number = models.IntegerField(null=False)
    description = models.CharField(max_length=1000, null=True)
    delivery_method = models.CharField(max_length=10, null=False)  # TODO: Do zmiany
    payment_method = models.CharField(max_length=10, null=False)  # TODO: Do zmiany
    status = models.CharField(max_length=10, null=False)  # TODO: Do zmiany
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
