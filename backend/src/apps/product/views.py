from rest_framework import viewsets

from apps.product.models import Discount
from apps.product.models import Category
from apps.product.models import Brand
from apps.product.models import Product
from apps.product.serializers import DiscountSerializer
from apps.product.serializers import CategorySerializer
from apps.product.serializers import BrandSerializer
from apps.product.serializers import ProductSerializer


class DiscountView(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
