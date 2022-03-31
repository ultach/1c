"""Top-level package for Reservation App."""

__app_name__ = "reservationapp"
__version__ = "0.1.0"

DATETIME_FORMAT = "%d/%m/%y %H:%M" 

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
    DUBLICATE_ERROR,
) = range(8)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "reservation id error",
    DUBLICATE_ERROR: "object cannot duplicate"
}
