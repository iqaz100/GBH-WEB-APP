from rest_framework import routers

from apps.product.views import DiscountView, CategoryView, BrandView, ProductView
from apps.cart.views import CartView
from apps.order.views import OrderView
from apps.client.views import ClientView, CompanyView
from apps.person.views import PersonView
from apps.address.views import AddressView
from apps.staff.views import StaffView, RoleView
from apps.user.views import UserView

router = routers.DefaultRouter()

router.register("discount", DiscountView, basename="discount")
router.register("category", CategoryView, basename="category")
router.register("brand", BrandView, basename="brand")
router.register("products", ProductView, basename="products")
router.register("cart", CartView, basename="cart")
router.register("order", OrderView, basename="order")
router.register("persons", PersonView, basename="persons")
router.register("clients", ClientView, basename="clients")
router.register("companies", CompanyView, basename="companies")
router.register("addresses", AddressView, basename="addresses")
router.register("staffs", StaffView, basename="staffs")
router.register("roles", RoleView, basename="roles")
router.register("users", UserView, basename="users")
