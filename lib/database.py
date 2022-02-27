import json

from lib.restaurant import Restaurant
from .address import Address
from .location import Location
# Database controller

# File string
class RestaurantDatabase():
    def __init__(self, path) -> None:
        file = open(path)
        data = json.load(file)
        self.restaurants = []
        for restaurant_obj in data["data"]:
            location = Location(restaurant_obj["geo"]["lat"], restaurant_obj["geo"]["lon"])
            address = Address(restaurant_obj["address"]["formatted"], location)
            restaurant = Restaurant(str(restaurant_obj["restaurant_id"]), restaurant_obj["restaurant_name"], address)
            self.restaurants.append(restaurant)

    def get_restaurant(self, id):
        return next(filter(lambda x: x.id == id, self.restaurants), None)

    def get_restaurants_available(self, user_location, distance):
        available_restaurants = []
        for restaurant in self.restaurants:
            restaurant_latitude = restaurant.address.location.latitude
            restaurant_longitude = restaurant.address.location.longitude
            restaurant_distance = Location.get_distance(user_location.latitude, restaurant_latitude, user_location.longitude, restaurant_longitude)
            if restaurant_distance <= distance:
                available_restaurants.append(restaurant)