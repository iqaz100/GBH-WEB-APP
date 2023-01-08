from rest_framework import serializers

from apps.product.models import Product
from apps.product.models import Brand
from apps.product.models import Category
from apps.product.models import Discount


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


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "description",
            "logo"
         )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description",
            "image"
        )


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = (
            "id",
            "code",
            "value_percentage",
            "value_flat",
            "expire_date",
            "type",
            "created_at",
            "modified_at"
        )
