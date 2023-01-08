from rest_framework import viewsets
from apps.order.serializers import OrderSerializer
from apps.order.models import Order


class OrderView(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
