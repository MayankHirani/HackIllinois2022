from .location import Location
from .address import Address
# Data class for restaurant
# Params: id (string), name (string), location (Location)
class Restaurant:
    def __init__(self, id, name, address) -> None:
        self.id = str(id)
        self.name = str(name)
        self.address = address
    
    def json(self):
        return { "id" : self.id, "name" : self.name, "address" : self.address.json() }