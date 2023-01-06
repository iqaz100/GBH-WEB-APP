import uuid

from django.db import models

from apps.address.models import Address


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=20, null=True)  # TODO: Do zmiany
    birth_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
