from rest_framework import serializers

from apps.staff.models import Staff, Role


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            "id",
            "user",
            "role",
            "created_at",
            "modified_at"
        )
        read_only_fields = ("id",)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            "name",
            "can_add_products",
            "can_modify_products"
        )
