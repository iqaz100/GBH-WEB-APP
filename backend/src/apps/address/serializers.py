from rest_framework import serializers

from apps.address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id",
            "street",
            "street_number",
            "apartment_number",
            "zip_code",
            "city",
            "country"
        )
        read_only_fields = ("id",)
