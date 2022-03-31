from . import TimeInterval


class Reservation:
    def __init__(self, room, interval, title=None, desc=None):
        self._room = room
        self._interval = interval
        self._title = title or None
        self._description = desc or None

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

    def __eq__(self, other):
        if self._room == other._room and self._interval.contains(other._interval):
            return True

        return False


def is_reservation_conflict(reservation_list, new_reservation):
    for reservation in reservation_list:
        time_interval = TimeInterval(reservation["StartTime"], reservation["EndTime"])
        if new_reservation == Reservation(reservation["RoomId"], time_interval):
            return True

    return False
