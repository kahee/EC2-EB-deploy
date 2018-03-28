from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from config.settings import secrets

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if User.objects.filter(username=secrets["SUPERUSER_USERNAME"]).exists():
            User.objects.create_superuser(
                username=secrets['SUPERUSER_USERNAME'],
                password=secrets['SUPERUSER_PASSWORD'],
                email=secrets['SUPERUSER_EMAIL'],
            )
