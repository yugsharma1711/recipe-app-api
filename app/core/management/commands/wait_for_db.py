from django.core.management.base import BaseCommand

import time

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for Database')
        db_up = False
        while db_up is False:
            try:
                self.check(database = ['default'])
                db_up  = True
            except(Psycopg2Error, OperationalError):
                self.stdout.write('Database Unvailable waiting for 1 second')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Available'))