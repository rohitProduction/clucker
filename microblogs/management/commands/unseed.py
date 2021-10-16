from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        User.objects.all().filter(is_superuser=False).filter(is_staff=False).delete()
