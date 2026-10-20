"""Location classes for the SIR simulation."""

class Location:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        """Add a person to the location."""
        self.people.append(person)

class Home(Location):
    pass

class Workplace(Location):
    def __init__(self, name, start_hour, end_hour):
        super().__init__(name)
        self.start_hour = start_hour
        self.end_hour = end_hour

    def is_open(self, hour):
        """Return whether the workplace is open at the given hour."""
        return self.start_hour <= hour < self.end_hour

class Office(Workplace):
    def __init__(self, name):
        super().__init__(name, start_hour=9, end_hour=17)

