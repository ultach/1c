### Set Up the Project

1. Create virtual environment:

   ```
   cd 1c/
   python -m venv ./venv
   source venv/bin/activate
   ```
2. Install Python dependencies `python -m pip install -r requirements.txt `
3. Init database  ``` python -m reservationapp init```

### Usage

###### To see list of avalible commends use

````
(venv) python -m reservationapp --help                        
Usage: reservationapp [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.

Commands:
  add-reservation   Add a new reservation.
  add-room          Add a new room.
  init              Initialize the schedule database.
  reservation-list  List all reservation.
```
````
