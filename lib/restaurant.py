from .location import Location
# Data class for restaurant
# Params: id (string), name (string), location (Location)
class Restaurant:
    def __init__(self, id, name, location) -> None:
        self.id = id
        self.name = name
        self.location = location