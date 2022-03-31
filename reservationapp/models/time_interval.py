from datetime import datetime, timedelta

from reservationapp import DATETIME_FORMAT


class TimeInterval:

    _start = None
    _end = None

    def __init__(self, start, minutes):
        self._start = datetime.strptime(start, DATETIME_FORMAT)

        # TODO:
        if isinstance(minutes, int):
            self._end = self._start + timedelta(minutes=minutes)
        else:
            self._end = datetime.strptime(minutes, DATETIME_FORMAT)

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

    def contains(self, time_interval) -> bool:
        return (
            (self._start <= time_interval._start) and (time_interval._start <= self._end)
        ) or (self._start <= time_interval._end and time_interval._end <= self._end)
