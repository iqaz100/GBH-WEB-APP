from rest_framework import routers

from apps.product.views import DiscountView
from apps.product.views import CategoryView
from apps.product.views import BrandView
from apps.product.views import ProductView
from apps.cart.views import CartView
from apps.order.views import OrderView


router = routers.DefaultRouter()

router.register("discount", DiscountView, basename="discount")
router.register("category", CategoryView, basename="category")
router.register("brand", BrandView, basename="brand")
router.register("products", ProductView, basename="products")
router.register("cart", CartView, basename="cart")
router.register("order", OrderView, basename="order")
