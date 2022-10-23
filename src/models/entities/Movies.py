from utils.Dateformat import Dateformat


class Movie:

    def __init__(self, id, title=None, duration=None, released=None) -> None:
        self.id = id
        self.title = title
        self.duration = duration
        self.released = released

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'released': Dateformat.convert_date(self.released)
        }
