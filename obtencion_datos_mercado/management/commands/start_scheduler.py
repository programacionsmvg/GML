# obtencion_datos_mercado/management/commands/start_scheduler.py
from django.core.management.base import BaseCommand
from obtencion_datos_mercado import jobs

class Command(BaseCommand):
    help = 'Starts the APScheduler jobs'

    def handle(self, *args, **options):
        jobs.start()
        self.stdout.write(self.style.SUCCESS('APScheduler started successfully'))