# Data class for attendee
# Params: id (string), emoji (char)
class Attendee:
    def __init__(self, id, emoji) -> None:
        self.id = id
        self.emoji = emoji