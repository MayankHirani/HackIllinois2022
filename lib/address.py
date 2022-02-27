from .location import Location
# Data class for address
# Params: address (string), location (Location)
class Address:
    def __init__(self, address, location) -> None:
        self.address = str(address)
        self.location = location
    
    def json(self):
        return { "address" : self.address, "location" : self.location.json() }