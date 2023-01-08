from rest_framework import viewsets

from apps.client.models import Client, Company
from apps.client.serializers import ClientSerializer, CompanySerializer


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
