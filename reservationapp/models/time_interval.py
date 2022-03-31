from datetime import datetime, timedelta

from reservationapp.constants import DATETIME_FORMAT


class TimeInterval:

    _start = None
    _end = None

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __init__(self, start, minutes):
        self._start = datetime.strptime(start, DATETIME_FORMAT)
        self._end = self._start + timedelta(minutes=minutes)

    @property
    def start(self) -> str:
        return self._start.strftime(DATETIME_FORMAT)

    @property
    def end(self) -> str:
        return self._end.strftime(DATETIME_FORMAT)

    def to_string(self) -> str:
        return " ".join(
            map(lambda dt: dt.strftime(DATETIME_FORMAT), [self._start, self._end])
        )    

    def is_time_inside(time):
        pass
