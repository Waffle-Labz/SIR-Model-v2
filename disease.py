"""Disease states used by the SIR simulation."""

from enum import Enum

class DiseaseState(Enum):
    SUSCEPTIBLE = "S"
    EXPOSED = "E"
    INFECTED = "I"
    RECOVERED = "R"
