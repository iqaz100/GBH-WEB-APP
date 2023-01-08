from rest_framework import viewsets

from apps.address.models import Address
from apps.address.serializers import AddressSerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
