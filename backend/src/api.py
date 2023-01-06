from rest_framework import routers

from apps.product.views import ProductView

router = routers.DefaultRouter()

router.register("products", ProductView, basename="products")
