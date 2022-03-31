"""This module provides the Reservation App database functionality."""

import json
import configparser
from pathlib import Path

from typing import Any, List, Dict, NamedTuple
from reservationapp import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath("." + Path.home().stem + "_schedule.json")


def get_database_path(config_file: Path) -> Path:
    """Return the current path to the schedule database."""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])


def init_database(db_path: Path) -> int:
    """Create the schedule database."""
    try:
        db_path.write_text(
            """
                        {
            "reservation": [],
            "room": []
            }
            """
        )
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR


class DBResponse(NamedTuple):
    reservation_list: List[Dict[str, Any]]
    room_list: List[Dict[str, Any]]
    error: int


class DatabaseHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def read_all(self) -> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    records = json.load(db)
                    return DBResponse(records["reservation"], records["room"], SUCCESS)
                except json.JSONDecodeError:  # Catch wrong JSON format
                    return DBResponse([], [], JSON_ERROR)
        except OSError:  # Catch file IO problems
            return DBResponse([], [], DB_READ_ERROR)

    def write_all(
        self, reservations_list: List[Dict[str, Any]], rooms_list: List[Dict[str, Any]]
    ) -> DBResponse:
        try:
            with self._db_path.open("w") as db:
                json.dump(
                    {"reservation": reservations_list, "room": rooms_list}, db, indent=4
                )
            return DBResponse(rooms_list, reservations_list, SUCCESS)
        except OSError:  # Catch file IO problems
            return DBResponse(reservations_list, DB_WRITE_ERROR)
