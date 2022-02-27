import uuid
from .attendee import Attendee
from .restaurant import Restaurant

# Meetup dataclass
# Params: id (str), start (datetime), creatorid (string), size(int), restaurant (Restaurant) attendees (Attendee[])
class Meetup:
    def __init__(self, creator, start, size, restaurant) -> None:
        self.id = str(uuid.uuid4())
        self.start = start
        self.creatorid = creator.id
        self.size = size
        self.restaurant = restaurant
        self.attendees = []
        self.attendees.append(creator)

    def add_attendee(self, id):
        if id not in self.attendees and len(self.attendees) < self.size:
            self.attendees.append(id)
    
    def remove_attendee(self, id, cache):
        if id in self.attendees:
            self.attendees.remove(id)
            if len(self.attendees) == 0:
                cache.meetups.remove(self)
            return True
        else:
            return False

    def json(self):
        attendees = []
        for attendee in self.attendees:
            attendees.append(attendee.json())
        return { "id" : self.id, "start" : str(self.start), "creatorid" : self.creatorid, "size" : self.size, "resaurant" : self.restaurant.json(), "attendees" : attendees }