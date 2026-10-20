"""Create the initial population and assign locations and disease states."""

from random import Random
import names

from config import (
    POPULATION_SIZE,
    INITIAL_INFECTED,
    INITIAL_RECOVERED,
)
from disease import DiseaseState
from person import Person
from location import Home, Office

def run(rng=None):
    """Create people, homes, workplaces, and initial disease states."""
    if rng is None:
        rng = Random()

    if INITIAL_INFECTED < 0 or INITIAL_RECOVERED < 0:
        raise ValueError("Initial disease counts cannot be negative")

    if INITIAL_INFECTED + INITIAL_RECOVERED > POPULATION_SIZE:
        raise ValueError("Initial infected and recovered counts exceed population")

    # Create the population.
    people = [
        Person(names.get_full_name())
        for _ in range(POPULATION_SIZE)
    ]

    # Assign people to homes, with up to four people per home.
    homes = []

    for start in range(0, POPULATION_SIZE, 4):
        home = Home(f"H{len(homes)}")

        for person in people[start:start + 4]:
            home.add_person(person)
            person.home = home

        homes.append(home)

    # Randomly assign people to workplaces, with up to ten per workplace.
    workplaces = []
    shuffled_people = people.copy()
    rng.shuffle(shuffled_people)

    for start in range(0, POPULATION_SIZE, 10):
        workplace = Office(f"O{len(workplaces)}")

        for person in shuffled_people[start:start + 10]:
            workplace.add_person(person)
            person.workplace = workplace

        workplaces.append(workplace)

    # Assign initial disease states.
    rng.shuffle(people)

    for person in people[:INITIAL_INFECTED]:
        person.disease_state = DiseaseState.INFECTED

    for person in people[
        INITIAL_INFECTED:INITIAL_INFECTED + INITIAL_RECOVERED
    ]:
        person.disease_state = DiseaseState.RECOVERED

    return people, homes, workplaces
