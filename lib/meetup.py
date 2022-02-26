import uuid
from .attendee import Attendee

# Meetup dataclass
# Params: id (str), start (datetime), creatorid (string), size(int), attendees (Attendee[])
class Meetup:
    def __init__(self, creator, start, size) -> None:
        self.id = str(uuid.uuid4())
        self.start = start
        self.creatorid = creator.id
        self.size = size
        self.attendees = []
        self.attendees.append(creator)