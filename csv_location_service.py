from location_service import LocationService
from coord import Coord
import csv

class CSVLocationService(LocationService):
    def get_lat_long(self, city, country):
        with open('worldcities.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['city_ascii'].lower() == city.lower() and row['country'].lower() == country.lower():
                    return Coord(float(row['lat']), float(row['lng']))
        return None
