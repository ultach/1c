class Room:
    _reservations = set()
    _capacity = None

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive, not {}".format(capacity))
        self._capacity = capacity

    def is_occupied(self, interval):
        pass

    def is_occupied(self, time):
        pass

    def cancel_reservation(self, interval_id):
        pass

    def cancel_reservation(self, reservation):
        pass

    def get_schedule(self):
        pass

    def add_reservation(self, interval):
        pass
