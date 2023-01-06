import uuid

from django.db import models


class Discount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=15, null=True)
    value_percentage = models.IntegerField(null=True)
    value_flat = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    expire_date = models.DateTimeField(null=True)
    type = models.CharField(max_length=15, null=False, default='P')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=True)
    logo = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    is_active = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    discount = models.ForeignKey(Discount, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)  # TODO: Do zmiany on_delete

    def __str__(self):
        return self.name
