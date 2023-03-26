from django.core.management import BaseCommand
from apps.product.models import Category, Product, Brand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.create_products_and_categories()

    def create_products_and_categories(self):
        hoodie = Category.objects.create(name='Bluzy', description='')
        t_shirt = Category.objects.create(name='Koszulki', description='')
        jacket = Category.objects.create(name='Kurtki', description='')
        pants = Category.objects.create(name='Spodnie', description='')
        shorts = Category.objects.create(name='Spodenki', description='')
        accessories = Category.objects.create(name='Akcesoria', description='')

        brand = Brand.objects.create(name='GBH')

        Product.objects.create(name='Bluza 1', price=99.99, category=hoodie, brand=brand)
        Product.objects.create(name='Bluza 2', price=79.99, category=hoodie, brand=brand)
        Product.objects.create(name='Bluza 3 - VIP', price=299.99, category=hoodie, brand=brand)

        Product.objects.create(name='Koszulka 1', price=69.99, category=t_shirt, brand=brand)
        Product.objects.create(name='Koszulka 2', price=39.99, category=t_shirt, brand=brand)
        Product.objects.create(name='Koszulka 3 - VIP', price=199.99, category=t_shirt, brand=brand)

        Product.objects.create(name='Kurtka 1', price=99.99, category=jacket, brand=brand)
        Product.objects.create(name='Kurtka 2', price=199.99, category=jacket, brand=brand)
        Product.objects.create(name='Kurtka 3 - VIP', price=499.99, category=jacket, brand=brand)

        Product.objects.create(name='Spodnie 1', price=99.99, category=pants, brand=brand)
        Product.objects.create(name='Spodnie 2', price=129.99, category=pants, brand=brand)
        Product.objects.create(name='Spodnie 3', price=299.99, category=pants, brand=brand)

        Product.objects.create(name='Krótkie spodenki', price=55.55, category=shorts, brand=brand)

        Product.objects.create(name='Czapka wpierdolka', price=21.37, category=accessories, brand=brand)

        print('Created categories, brands and products')
