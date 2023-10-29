from service.location_service import LocationService
from service.coord import Coord

class MockLocationService(LocationService):
    def get_lat_long(self, city, country):
        return Coord(0, 0) # The Coord Class works and does not give any 
