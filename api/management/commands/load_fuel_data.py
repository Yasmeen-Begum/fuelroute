from pathlib import Path

import pandas as pd
from django.core.management.base import BaseCommand
from ...models import FuelStation

class Command(BaseCommand):
    help = "Load fuel stations from CSV"

    def handle(self, *args, **kwargs):
        df = pd.read_csv("C:/Users/DELL/Music/internshala/spot/fuelroute/api/management/commands/fuel-prices-for-be-assessment.csv") # use csv file path fuel-prices-for-be-assessment.csv
        for _, row in df.iterrows():
            FuelStation.objects.create(
                name=row["Truckstop Name"],
                latitude=0.0,
                longitude=0.0,
                price_per_gallon=row["Retail Price"]
            )
        self.stdout.write(self.style.SUCCESS("Fuel data loaded"))
