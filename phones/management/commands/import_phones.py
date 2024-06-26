import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
             
            for element in  phone_reader:
                Phone.name = element[0]
                Phone.price = element[1]
                Phone.image = element[2]
                Phone.release_date = element[3]
                Phone.lte_existst = element[4]
                Phone.slug = element[5]
