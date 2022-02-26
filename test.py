from lib.database import RestaurantDatabase

db = RestaurantDatabase("./data/restaurant_data.json")
for res in db.restaurants:
    print(res.name)