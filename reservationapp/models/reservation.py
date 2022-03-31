class Reservation:
    def __init__(self):
        self._room = None
        self._interval = None
        self._title = None
        self._description = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def title(self):
        return title

    @description.setter
    def title(self, new_title):
        self._title = new_title

    def get_room_id(self):
        return self._room.get_id()

    def get_interval_id(self):
        return self._interval.get_id()
