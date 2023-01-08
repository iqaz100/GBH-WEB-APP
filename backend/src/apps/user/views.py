from rest_framework import viewsets

from apps.user.models import User
from apps.user.serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
