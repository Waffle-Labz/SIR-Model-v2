"""Keeps track of time within the simulation."""

class Clock:
    def __init__(self, start_hour=0):
        self.hour = start_hour
        self.day = 0

    def tick(self):
        """Advance the simulation by one hour."""
        self.hour += 1

        if self.hour >= 24:
            self.hour = 0
            self.day += 1
