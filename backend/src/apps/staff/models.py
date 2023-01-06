import uuid

from django.db import models

from apps.user.models import User


class Role(models.Model):
    name = models.CharField(max_length=30)
    can_add_products = models.BooleanField(default=False)
    can_modify_products = models.BooleanField(default=False)


class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
