import uuid
from .location import Location
from .address import Address
from .attendee import Attendee
from .restaurant import Restaurant

# Meetup dataclass
# Params: id (str), start (datetime), creatorid (string), size(int), restaurant (Restaurant) attendees (Attendee[])
class Meetup:
    def __init__(self, creator, start, size, restaurant) -> None:
        self.id = str(uuid.uuid4())
        self.start = start
        self.creatorid = str(creator.id)
        self.size = int(size)
        self.restaurant = restaurant
        self.attendees = []
        self.attendees.append(creator)

    def add_attendee(self, attendee):
        for att in self.attendees:
            if (att.id == attendee.id): return
        if len(self.attendees) < self.size:
            self.attendees.append(attendee)
    
    def remove_attendee(self, id, cache):
        for attendee in self.attendees:
            if (attendee.id == str(id)):
                self.attendees.remove(attendee)
        if len(self.attendees) == 0:
            cache.meetups.remove(self)

    def json(self):
        attendees = []
        for attendee in self.attendees:
            attendees.append(attendee.json())
        return { "id" : self.id, "start" : str(self.start), "creatorid" : self.creatorid, "size" : self.size, "restaurant" : self.restaurant.json(), "attendees" : attendees }