from rest_framework import viewsets
from apps.cart.serializers import CartSerializer
from apps.cart.models import Cart


class CartView(viewsets.ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
