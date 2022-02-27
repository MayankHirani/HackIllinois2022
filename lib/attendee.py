# Data class for attendee
# Params: id (string), emoji (char)
class Attendee:
    def __init__(self, id, emoji) -> None:
        self.id = id
        self.emoji = emoji

    def __eq__(self, other):
        if isinstance(other, Attendee):
            return self.id == other.id
        return False
    
    def __ne__(self, other):
        if isinstance(other, Attendee):
            return self.id != other.id
        return False

    def json(self):
        return { "id" : self.id, "emoji" : self.emoji }