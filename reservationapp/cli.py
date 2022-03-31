"""This module provides the Reservation App CLI."""
# reservationapp/cli.py

from pathlib import Path
from typing import List, Optional

import typer

from reservationapp import ERRORS, __app_name__, __version__, config, database, planner

app = typer.Typer()


@app.command()
def init(
    db_path: str = typer.Option(
        str(database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="schedule database location?",
    ),
) -> None:
    """Initialize the schedule database."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"The schedule database is {db_path}", fg=typer.colors.GREEN)


def get_planner() -> planner.Planner:
    if config.CONFIG_FILE_PATH.exists():
        db_path = database.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please, run "reservationapp init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    if db_path.exists():
        return planner.Planner(db_path)
    else:
        typer.secho(
            'Database not found. Please, run "reservationapp init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)


@app.command()
def add_reservation(
    room_id: int = typer.Argument(...),
    start_time: str = typer.Argument(...),
    duration_in_minutes: int = typer.Option(45, "--duration", "-d", min=15, max=120),
    title: str = typer.Argument(...),
    description: List[str] = typer.Argument(...),
) -> None:
    """Add a new reservation."""
    pl = get_planner()
    reservation, error = pl.add_reservation(
        room_id, start_time, duration_in_minutes, title, description
    )
    if error:
        typer.secho(
            f'Adding reservation failed with "{ERRORS[error]}"', fg=typer.colors.RED
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            f"""Room #{reservation['RoomId']} was reservated """
            f"""for time: {start_time}.""",
            fg=typer.colors.GREEN,
        )


@app.command(name="reservation-list")
def list_all() -> None:
    """List all reservation."""
    pl = get_planner()
    reservation_list = pl.get_reservation_list()
    if len(reservation_list) == 0:
        typer.secho("There are no reservations in the schedule yet.", fg=typer.colors.RED)
        raise typer.Exit()
    typer.secho("\nreservation list:\n", fg=typer.colors.BLUE, bold=True)
    columns = (
        "| ID  ",
        "| RoomId  ",
        "| StartTime ",
        "| EndTime ",
        "| Title  ",
        "| Description  ",
    )
    headers = "".join(columns)
    typer.secho(headers, fg=typer.colors.BLUE, bold=True)
    typer.secho("-" * len(headers), fg=typer.colors.BLUE)
    for id, reservation in enumerate(reservation_list, 1):
        room_id, start, end, title, desc = reservation.values()
        typer.secho(
            f"{id}{(len(columns[0]) - len(str(id))) * ' '}"
            f"| {room_id}{(len(columns[1]) - len(str(room_id)) - 2) * ' '}"
            f"| {start}{(len(columns[2]) - len(str(start))) * ' '}"
            f"| {end}{(len(columns[2]) - len(str(end))) * ' '}"
            f"| {title}{(len(columns[2]) - len(str(title))) * ' '}"
            f"| {desc}",
            fg=typer.colors.BLUE,
        )
    typer.secho("-" * len(headers) + "\n", fg=typer.colors.BLUE)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
