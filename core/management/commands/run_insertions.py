 
from django.core.management.base import BaseCommand
from core.views import run_concurrent_insertions

class Command(BaseCommand):
    help = 'Run concurrent insertions into multiple databases'

    def handle(self, *args, **kwargs):
        run_concurrent_insertions()
