from lib.attendee import Attendee
from lib.meetup_cache import MeetupCache
from lib.database import RestaurantDatabase

db = RestaurantDatabase("data/restaurant_data.json")

cache = MeetupCache()

attendee = Attendee("101", '🥰')

cache.create_meetup(db.get_restaurant("4006963788249733"), "3:00", attendee, 4)

ret = []
for meetup in cache.get_user_meetups(attendee.id):
    ret.append(meetup.json())

print(ret)