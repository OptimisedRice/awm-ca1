from io import StringIO

from app.models import Toilet
import csv
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point


class Command(BaseCommand):
    help = 'load public toilet data from csv file'

    def handle(self, *args, **options):
        Toilet.objects.all().delete() # delete toilet data

        with open("app/data/public-toilets-dcc-2021-updated.csv", 'r') as file:
            content = file.read().replace('\n"', '"')
            csv_reader = csv.reader(StringIO(content))
            next(csv_reader, None)
            for row in csv_reader:
                toilet = Toilet(
                    id=row[0],
                    location=row[1],
                    opening_hours=row[2],
                    latitude=row[3],
                    longitude=row[4]
                )
                toilet.save()

        print("Toilets loaded successfully")
