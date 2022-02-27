from .address import Location
# Data class for restaurant
# Params: id (string), name (string), location (Location)
class Restaurant:
    def __init__(self, id, name, address) -> None:
        self.id = str(id)
        self.name = str(name)
        self.address = str(address)
    
    def json(self):
        return { "id" : self.id, "name" : self.name, "address" : self.address.json() }