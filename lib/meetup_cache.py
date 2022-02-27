from .meetup import Meetup
from .location import get_distance
from datetime import datetime

class MeetupCache:
    def __init__(self) -> None:
        self.meetups = []

    def get_meetup(self, id):
        return next(filter(lambda x: x.id == str(id), self.meetups), None)

    def get_user_meetups(self, id):
        events = []
        for event in self.meetups:
            if next(filter(lambda x: x.id == str(id), event.attendees), None) != None:
                events.append(event)
        return events

    def get_available_meetups(self, id, user_location, max_distance):
        available_meetups = []
        current_meetups = self.get_user_meetups(id)
        current_times = []
        for event in current_meetups:
            current_times.append(event.start)
        for event in self.meetups:
            event_latitude = event.restaurant.address.location.latitude
            event_longitude = event.restaurant.address.location.longitude
            distance = get_distance(user_location.latitude, event_latitude, user_location.longitude, event_longitude)
            if event not in current_meetups and event.start not in current_times and distance <= max_distance:
                available_meetups.append(event)
        return available_meetups

    def create_meetup(self, restaurant, time, creator, size):
        start = datetime.strptime(time, '%H:%M')
        self.meetups.append(Meetup(creator, start, int(size), restaurant))




                