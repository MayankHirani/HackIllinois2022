from .meetup import Meetup
from .location import Location, get_distance
from .address import Address
from .attendee import Attendee
from .restaurant import Restaurant
from datetime import datetime

class MeetupCache:
    def __init__(self) -> None:
        self.meetups = []

    def get_meetup(self, id):
        meet = None
        for meetup in self.meetups:
            if (meetup.id == str(id)): meet = meetup
        return meet

    def get_user_meetups(self, id):
        meetups = []
        for meetup in self.meetups:
            for attendee in meetup.attendees:
                if (attendee.id == str(id)): meetups.append(meetup)
        return meetups

    def get_available_meetups(self, id, user_location, max_distance):
        available_meetups = []
        current_meetups = self.get_user_meetups(str(id))
        current_times = []
        for event in current_meetups:
            current_times.append(event.start)
        for event in self.meetups:
            event_latitude = float(event.restaurant.address.location.latitude)
            event_longitude = float(event.restaurant.address.location.longitude)
            distance = get_distance(user_location.latitude, event_latitude, user_location.longitude, event_longitude)
            if event not in current_meetups and event.start not in current_times and distance <= max_distance:
                available_meetups.append(event)
        return available_meetups

    def create_meetup(self, restaurant, time, creator, size):
        start = datetime.strptime(time, '%H:%M')
        self.meetups.append(Meetup(creator, start, int(size), restaurant))




                