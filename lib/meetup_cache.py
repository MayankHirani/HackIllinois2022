from .meetup import Meetup

class MeetupCache:
    def __init__(self) -> None:
        self.meetups = []
    
    # TODO: function to get participating meetups by user id -> array of meetup ids
    # TODO: function to get non-participating meetups by user id, distance, conflicts -> approriate array of meetup ids

    def get_meetup(self, id):
        return next(filter(lambda x: x.id == id, self.meetups), None)