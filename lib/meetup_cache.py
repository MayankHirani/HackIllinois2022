from .meetup import Meetup
from math import radians, cos, sin, asin, sqrt, pi
from datetime import date

class MeetupCache:
    def __init__(self) -> None:
        self.meetups = []
    
    # TODO: function to get participating meetups by user id -> array of meetup ids
    # TODO: function to get non-participating meetups by user id, distance, conflicts -> approriate array of meetup ids

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
            event_latitude = event.restaurant.adress.location.latitude
            event_longitude = event.restaurant.adress.location.longitude
            distance = self.get_distance(user_location.latitude, event_latitude, user_location.longitude, event_longitude)
            if event not in current_meetups and event.time not in current_times and distance <= max_distance:
                available_meetups.append(event)

    #for get_available_meetups
    def distance(lat1, lat2, lon1, lon2):
     
        lon1 *= pi/180
        lon2 *= pi/180
        lat1 *= pi/180
        lat2 *= pi/180

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))
        return(c * 3956)

    def create_meetup(self, restaurant, time, creator, size):
        start = date.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
        self.meetups.append(Meetup(creator, start, size, restaurant))




                