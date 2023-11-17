from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    help = 'Creates django admin with provided arguments'

    def add_arguments(self, parser):
        parser.add_argument('-e', '--email', type=str)
        parser.add_argument('-p', '--password', type=str)
        parser.add_argument('-u', '--username', type=str)

    def handle(self, *args, **options):
        email = options.get('email')
        password = options.get('password')
        username = options.get('username')
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            stdout = f'Superuser successfully created with email: {email} and password: {password}'
            self.stdout.write(self.style.SUCCESS(stdout))
