from .meetup import Meetup
from .location import get_distance
from datetime import datetime

class MeetupCache:
    def __init__(self) -> None:
        self.meetups = []

    def sort_meetups(self, user_location):
        distances = []
        for event in self.meetups:
            event_latitude = event.restaurant.address.location.latitude
            event_longitude = event.restaurant.address.location.longitude
            distance = get_distance(user_location.latitude, event_latitude, user_location.longitude, event_longitude)
            distances.append(distance)

        for i in range(1, len(distances)):
            x = distances[i]
            y = self.meetups[i]
            j = i - 1
            while j >= 0 and x < distances[j]:
                distances[j+1] = distances[j]
                j -= 1
            distances[j+1] = x
            self.meetups[j + 1] = y

            

    def get_meetup(self, id):
        return next(filter(lambda x: x.id == id, self.meetups), None)

    def get_user_meetups(self, id):
        events = []
        for event in self.meetups:
            if id in event.attendees:
                events.append(event)
        return events

    def get_available_meetups(self, id, user_location, max_distance):
        available_meetups = []
        current_meetups = self.get_user_meetups(self, id)
        current_times = []
        for event in current_meetups:
            current_times.append(event.start)
        for event in self.meetups:
            event_latitude = event.restaurant.address.location.latitude
            event_longitude = event.restaurant.address.location.longitude
            distance = get_distance(user_location.latitude, event_latitude, user_location.longitude, event_longitude)
            if event not in current_meetups and event.time not in current_times and distance <= max_distance:
                available_meetups.append(event)
        return available_meetups

    def create_meetup(self, restaurant, time, creator, size):
        start = datetime.strptime(time, '%H:%M')
        self.meetups.append(Meetup(creator, start, size, restaurant))




                