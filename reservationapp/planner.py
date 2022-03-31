"""This module provides the Reservation App model-controller."""
from pathlib import Path
from typing import List, Any, Set, NamedTuple

from .models import Reservation, TimeInterval, Room, is_reservation_conflict
from reservationapp.database import DB_READ_ERROR, DatabaseHandler
from reservationapp import DUBLICATE_ERROR


class CurrentReservation(NamedTuple):
    reservation: Set[Reservation]
    error: int


class CurrentRoom(NamedTuple):
    reservation: Set[Room]
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
    ) -> CurrentReservation:
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

        read = self._db_handler.read_all()

        if read.error == DB_READ_ERROR:
            return CurrentReservation(reservation, read.error)

        if is_reservation_conflict(
            read.reservation_list, Reservation(room_id, time_interval)
        ):
            return CurrentReservation(reservation, DUBLICATE_ERROR)
        read.reservation_list.append(reservation)
        write = self._db_handler.write_all(read.reservation_list, read.room_list)
        return CurrentReservation(reservation, write.error)

    def add_room(self, room_id: int, capacity: int) -> CurrentRoom:
        """Add a new reservation to the database."""
        room = {"RoomId": room_id, "Capacity": capacity}

        read = self._db_handler.read_all()

        if read.error == DB_READ_ERROR:
            return CurrentRoom(reservation, read.error)

        read.room_list.append(room)
        write = self._db_handler.write_all(read.reservation_list, read.room_list)
        return CurrentRoom(room, write.error)

    def get_reservation_list(self) -> List:
        """Return the current reservation list."""
        read = self._db_handler.read_all()
        return read.reservation_list

    def get_recommendation(
        self, time_interval: TimeInterval, capacity: int
    ) -> List[Room]:
        pass

    def get_available_rooms(self, time_interval: TimeInterval):
        pass
