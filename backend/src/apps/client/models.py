import uuid

from django.db import models

from apps.address.models import Address
from apps.user.models import User


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nip = models.IntegerField(null=False)
    name = models.CharField(max_length=100, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
