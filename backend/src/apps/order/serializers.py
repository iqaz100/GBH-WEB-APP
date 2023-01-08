from rest_framework import serializers

from apps.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "client",
            "address",
            "order_number",
            "description",
            "delivery_method",
            "payment_method",
            "status",
            "created_at",
            "modified_at"
        )
        read_only_fields = ("id",)
