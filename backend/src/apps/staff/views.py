from rest_framework import viewsets

from apps.staff.models import Staff, Role
from apps.staff.serializers import StaffSerializer, RoleSerializer


class StaffView(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
