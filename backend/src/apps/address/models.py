import uuid

from django.db import models


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=100, null=True)
    street_number = models.CharField(max_length=10, null=False)
    apartment_number = models.CharField(max_length=10, null=True)
    zip_code = models.CharField(max_length=10, null=False)
    city = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False, default='Poland')
