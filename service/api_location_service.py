from service.location_service import LocationService
from service.coord import Coord
import requests

class APILocationService(LocationService):
    def get_lat_long(self, city, country):
        url = f'https://nominatim.openstreetmap.org/search?q={city},{country}&format=json'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                return Coord(float(data[0]['lat']), float(data[0]['lon']))
        return None
