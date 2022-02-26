# Data class for location
# Params: address (string), latitude (float), longitude (float)
class Location:
    def __init__(self, address, latitude, longitude) -> None:
        self.address = address
        self.latitude = latitude
        self.longitude = longitude