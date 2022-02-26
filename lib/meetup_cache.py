from .meetup import Meetup

class MeetupCache:
    def __init__(self) -> None:
        self.meetups = []
    
    def get_meetup(self, id):
        return next(filter(lambda x: x.id == id, self.meetups), None)