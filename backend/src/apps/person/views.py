from rest_framework import viewsets

from apps.person.models import Person
from apps.person.serializers import PersonSerializer


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
