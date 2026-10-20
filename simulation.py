
"""Core agent-based SEIR simulation."""

from random import Random

from config import (
    HOURS_PER_DAY,
    SIMULATION_STEPS,
    INFECTION_PROBABILITY,
    RECOVERY_PROBABILITY,
    MAX_INFECTION_PERIOD_DAYS,
    LATE_RECOVERY_PROBABILITY,
    LATENT_PERIOD_HOURS,
)
from clock import Clock
from disease import DiseaseState
from initialise import run as initialise_population


class Simulation:
    def __init__(self, seed=None):
        self.rng = Random(seed)

        self.people, self.homes, self.workplaces = (
            initialise_population(self.rng)
        )

        self.clock = Clock()
        self.history = []

        self.max_infection_hours = (
            MAX_INFECTION_PERIOD_DAYS * HOURS_PER_DAY
        )

        self.record_statistics()

    def get_location(self, person):
        """Determine where a person is at the current hour."""
        if person.workplace is not None:
            if person.workplace.is_open(self.clock.hour):
                return person.workplace

        return person.home

    def record_statistics(self):
        """Record the current population counts."""
        counts = {
            DiseaseState.SUSCEPTIBLE: 0,
            DiseaseState.EXPOSED: 0,
            DiseaseState.INFECTED: 0,
            DiseaseState.RECOVERED: 0,
        }

        for person in self.people:
            counts[person.disease_state] += 1

        self.history.append({
            "time_hours": (
                self.clock.day * HOURS_PER_DAY + self.clock.hour
            ),
            "day": self.clock.day,
            "hour": self.clock.hour,
            "susceptible": counts[DiseaseState.SUSCEPTIBLE],
            "exposed": counts[DiseaseState.EXPOSED],
            "infected": counts[DiseaseState.INFECTED],
            "recovered": counts[DiseaseState.RECOVERED],
        })

    def step(self):
        """Advance the simulation by one hour."""
        # Group people by their current location.
        occupants = {}

        for person in self.people:
            location = self.get_location(person)
            occupants.setdefault(location, []).append(person)

        # Snapshot disease states at the start of the hour.
        infected_people = [
            person for person in self.people
            if person.disease_state == DiseaseState.INFECTED
        ]

        exposed_people = [
            person for person in self.people
            if person.disease_state == DiseaseState.EXPOSED
        ]

        susceptible_people = [
            person for person in self.people
            if person.disease_state == DiseaseState.SUSCEPTIBLE
        ]

        newly_exposed = set()
        newly_infected = set()
        newly_recovered = set()

        # Transmission: only people already infectious can transmit.
        for location_people in occupants.values():
            infected_here = [
                person for person in location_people
                if person in infected_people
            ]

            susceptible_here = [
                person for person in location_people
                if person in susceptible_people
            ]

            for infected in infected_here:
                for susceptible in susceptible_here:
                    if self.rng.random() < INFECTION_PROBABILITY:
                        newly_exposed.add(susceptible)

        # Progress the latent period.
        for person in exposed_people:
            person.exposure_duration_hours += 1

            if (
                person.exposure_duration_hours >= LATENT_PERIOD_HOURS
            ):
                newly_infected.add(person)

        # Progress infection and check for recovery.
        for person in infected_people:
            person.infection_duration_hours += 1

            if self.rng.random() < RECOVERY_PROBABILITY:
                newly_recovered.add(person)

            elif (
                person.infection_duration_hours
                >= self.max_infection_hours
                and self.rng.random() < LATE_RECOVERY_PROBABILITY
            ):
                newly_recovered.add(person)

        # Apply state changes after all processes have been evaluated.
        for person in newly_exposed:
            person.disease_state = DiseaseState.EXPOSED
            person.exposure_duration_hours = 0

        for person in newly_infected:
            person.disease_state = DiseaseState.INFECTED
            person.infection_duration_hours = 0

        for person in newly_recovered:
            person.disease_state = DiseaseState.RECOVERED

        # Advance time and record the completed step.
        self.clock.tick()
        self.record_statistics()

    def run(self):
        """Run the simulation for its configured duration."""
        for _ in range(SIMULATION_STEPS):
            self.step()

        return self.history
