from rest_framework import serializers

from apps.person.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            "id",
            "first_name",
            "last_name",
            "address",
            "phone_number",
            "email",
            "gender",
            "birth_date",
            "created_at",
            "modified_at"
        )
        read_only_fields = ("id",)
