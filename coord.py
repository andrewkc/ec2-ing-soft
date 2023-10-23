from math import radians
from haversine import haversine

class Coord:
    def __init__(self, la, lo):
        self.la = la
        self.lo = lo
    
    def distance_to(self, other_coord):
        lat1 = radians(self.la)
        lon1 = radians(self.lo)
        lat2 = radians(other_coord.la)
        lon2 = radians(other_coord.lo)
        distance = haversine((lat1, lon1), (lat2, lon2))
        return distance
