from math import radians, cos, sin, asin, sqrt, pi

# latitude (float), longitude (float)
class Location:
    def __init__(self, lat, lon) -> None:
        self.latitude = float(lat)
        self.longitude = float(lon)

    def json(self):
        return { "latitude" : self.latitude, "longitude" : self.longitude }
    
def get_distance(lat1, lat2, lon1, lon2):
    lon1 *= pi/180
    lon2 *= pi/180
    lat1 *= pi/180
    lat2 *= pi/180

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    return(c * 3956)
