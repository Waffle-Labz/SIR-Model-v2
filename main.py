"""Entry point for the SIR simulation."""

from simulation import Simulation
from visualisation import plot_sir

def main():
    simulation = Simulation()

    print("Running SIR simulation...")
    history = simulation.run()

    plot_sir(history)
    

if __name__ == "__main__":
    main()
