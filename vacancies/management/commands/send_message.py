from django.core.management.base import BaseCommand
import time
from vacancies.service.bot import send_bot


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start_time = time.time()
        send_bot()
        self.stdout.write("--- %s seconds ---" % (time.time() - start_time))
