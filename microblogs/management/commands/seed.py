from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from faker.providers.misc import Provider
from faker.providers.person import Provider
from faker.providers.internet import Provider
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        for i in range(100):
            user = User()
            user.username = self.faker.name()
            user.first_name = self.faker.first_name()
            user.last_name = self.faker.last_name()
            user.email = self.faker.email()
            user.bio = self.faker.text()
            user.save()

            """
            User.objects.create_user(
            username = self.faker.name(),
            first_name = self.faker.first_name(),
            last_name = self.faker.last_name(),
            email = self.faker.email()
            bio = self.faker.text()
            password = self.faker.password()
            )
            """
