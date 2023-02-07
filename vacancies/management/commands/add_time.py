from django.core.management.base import BaseCommand
import time
from vacancies.models import Time


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start_time = time.time()
        for i in range(0, 24, 1):
            t = f"{str(i)}:00:00"
            Time.objects.create(time=t)


        self.stdout.write("--- %s seconds ---" % (time.time() - start_time))
