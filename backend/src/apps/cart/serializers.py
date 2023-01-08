from rest_framework import serializers

from apps.cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            "id",
            "created_at",
            "modified_at",
            "discount_id",
            "user_id"

        )
        read_only_fields = ("id",)
