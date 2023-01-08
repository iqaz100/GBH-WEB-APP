from rest_framework import serializers

from apps.client.models import Client, Company


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "user"
        )
        read_only_fields = ("id",)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "id",
            "nip",
            "name",
            "address",
            "client"
        )
        read_only_fields = ("id",)
