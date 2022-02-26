from .meetup import Meetup

class MeetupCache:
    def __init__(self) -> None:
        self.meetups = []
    
    # TODO: function to get participating meetups by user id -> array of meetup ids
    # TODO: function to get non-participating meetups by user id, distance, conflicts -> approriate array of meetup ids

    def get_meetup(self, id):
        return next(filter(lambda x: x.id == id, self.meetups), None)

    def get_user_meetups(self, attendee):
        meetup_ids = []
        for event in self.meetups:
            if attendee in event.attendees:
                meetup_ids.append(event)
        return meetup_ids

    # assumes attendee has a latitude and longitude
    def get_available_meetups(self, attendee):
        available_meetups = []
        current_meetups = get_attendee_meetups(self, attendee)
        current_times = []
        for event in current_meetups:
            current_times.append(event.start)
        distance = event
        for event in self.meetups:
            if event not in current_meetups and event.time not in current_times:
                