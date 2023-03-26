from django.core.management import BaseCommand

from apps.client.models import Client
from apps.staff.models import Staff, Role
from apps.user.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.create_users()

    def create_users(self):
        user_client = User.objects.create(email='client_testowy1@gbh.com.pl')
        user2 = User.objects.create(email='admin@gbh.com.pl')

        Client.objects.create(user=user_client)

        role_admin = Role.objects.create(can_add_products=True, can_modify_products=True)
        Staff.objects.create(user=user2, role=role_admin)

        print('Created users, clients and staff')
