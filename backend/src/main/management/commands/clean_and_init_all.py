
"""
Funkcja czyszcząca bazę danych i uzupełniająca ją nowymi danymi

Wywołanie (backend/src): python manage.py clean_and_init_all
"""
from django.core.management import BaseCommand
from django.core import management


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        management.call_command('flush', '--noinput')
        management.call_command('generate_products')
        management.call_command('generate_users')
