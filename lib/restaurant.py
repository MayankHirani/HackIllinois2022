from .address import Location
# Data class for restaurant
# Params: id (string), name (string), location (Location)
class Restaurant:
    def __init__(self, id, name, address) -> None:
        self.id = id
        self.name = name
        self.address = address
    
    def json(self):
        return { "id" : self.id, "name" : self.name, "address" : self.address.json() }