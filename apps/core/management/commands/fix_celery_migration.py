from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Fixes django_celery_results migration issue with Djongo'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(
            'Faking problematic django_celery_results migrations...'
        ))
        
        # First, fake the migration up to the problematic one
        call_command('migrate', 'django_celery_results', '0005_taskresult_worker', fake=True)
        
        # Then, fake the problematic migration
        call_command('migrate', 'django_celery_results', '0006_taskresult_date_created', fake=True)
        
        # Continue with remaining migrations
        call_command('migrate', 'django_celery_results', fake_initial=True)
        
        self.stdout.write(self.style.SUCCESS(
            'Successfully faked django_celery_results migrations!'
        ))
        
        self.stdout.write(self.style.WARNING(
            'Note: You are using Redis for Celery results, not the database.'
        ))
