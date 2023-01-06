from rest_framework import serializers

from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "is_active",
            "brand_id",
            "created_at",
            "modified_at",
            "category"
        )
        read_only_fields = ("id",)
