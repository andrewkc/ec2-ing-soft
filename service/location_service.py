from abc import ABC, abstractmethod
from service.coord import Coord

class LocationService(ABC):
    @abstractmethod
    def get_lat_long(self, city, country):
        pass

    def calculate_distance(self, city1, country1, city2, country2):
        coord1 = self.get_lat_long(city1, country1)
        coord2 = self.get_lat_long(city2, country2)

        if coord1 is not None and coord2 is not None:
            return coord1.distance_to(coord2)
        else:
            return None
