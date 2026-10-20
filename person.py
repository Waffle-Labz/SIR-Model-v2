"""Individual agents in the SIR simulation."""

from disease import DiseaseState

class Person:
    def __init__(self, name, home=None, workplace=None):
        self.name = name

        # Assigned locations
        self.home = home
        self.workplace = workplace

        # Disease state
        self.disease_state = DiseaseState.SUSCEPTIBLE
        self.exposure_duration_hours = 0
        self.infection_duration_hours = 0
