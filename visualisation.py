"""Visualisation tools for the SIR simulation."""

import matplotlib.pyplot as plt


def plot_sir(history):
    """Plot susceptible, infected, and recovered population over time."""
    days = [entry["time_hours"] / 24 for entry in history]
    susceptible = [entry["susceptible"] for entry in history]
    exposed = [entry["exposed"] for entry in history]
    infected = [entry["infected"] for entry in history]
    recovered = [entry["recovered"] for entry in history]

    plt.figure(figsize=(12, 6))

    plt.plot(days, susceptible, label="Susceptible", color="blue")
    plt.plot(days, exposed, label="Exposed", color="orange")
    plt.plot(days, infected, label="Infected", color="red")
    plt.plot(days, recovered, label="Recovered", color="green")

    plt.title("SIR Epidemic Simulation")
    plt.xlabel("Time (days)")
    plt.ylabel("Population")
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()
