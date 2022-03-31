"""This module provides the Reservation App model-controller."""
from pathlib import Path
from typing import List, Any, Set, NamedTuple

from .models import Reservation, TimeInterval, Room
from reservationapp.database import DB_READ_ERROR, DatabaseHandler


class CurrentSchedule(NamedTuple):
    reservation: Set[Reservation]
    error: int


class Planner:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)

    def add_reservation(
        self,
        room_id: int,
        start_time: str,
        duration_in_minutes: int,
        title,
        description: List[str],
    ) -> CurrentSchedule:
        """Add a new reservation to the database."""

        description_text = " ".join(description)
        if not description_text.endswith("."):
            description_text += "."
        
        time_interval = TimeInterval(start_time, duration_in_minutes)
        reservation = {
            "RoomId": room_id,
            "StartTime": time_interval.start,
            "EndTime": time_interval.end,
            "Title": title,
            "Description": description_text,
        }

        read = self._db_handler.read_reservations()
        print(read.available_rooms)
        if read.error == DB_READ_ERROR:
            return CurrentSchedule(reservation, read.error)
        read.reservation_list.append(reservation)
        write = self._db_handler.write_reservations(read.reservation_list)
        return CurrentSchedule(reservation, write.error)


    def add_room(self, room_id: int, capacity: int):
        pass

    def get_reservation_list(self) -> List:
        """Return the current reservation list."""
        read = self._db_handler.read_reservations()
        return read.reservation_list

    def get_recommendation(self, time_interval: TimeInterval):
        pass
