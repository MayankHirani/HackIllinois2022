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