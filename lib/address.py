from .location import Location
# Data class for address
# Params: address (string), location (Location)
class Address:
    def __init__(self, address, location) -> None:
        self.address = address
        self.location = location