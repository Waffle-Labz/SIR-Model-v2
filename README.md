# SIR-Model-v2

A Python-based agent simulation of infectious disease transmission using the SEIR epidemiological model. The simulation represents individuals as agents who interact within homes and workplaces, with disease progression tracked over time.

The project explores agent-based modelling, stochastic processes, object-oriented programming and the simulation of dynamic systems.

## Features

- **Agent-based population:** Individuals are represented as separate objects with their own disease states, infection durations and assigned locations.
- **SEIR disease model:** Individuals progress through four states:
  - **Susceptible (S):** Can become infected through contact with an infectious individual.
  - **Exposed (E):** Has been infected but is not yet infectious.
  - **Infected (I):** Can transmit the disease and may recover.
  - **Recovered (R):** No longer infectious and assumed immune for the remainder of the simulation.
- **Probabilistic transmission:** Transmission is determined by a configurable probability for each infectious–susceptible contact.
- **Disease progression:** Exposed individuals become infectious after a configurable latent period. Recovery is probabilistic, with an additional recovery mechanism for infections that exceed a specified duration.
- **Location-based interactions:** Individuals are assigned to homes and workplaces. Workplace opening hours determine where individuals spend each simulated hour.
- **Hourly simulation:** A simulation clock tracks the hour and day.
- **Statistical tracking:** Population counts are recorded throughout the simulation.
- **Visualisation:** Matplotlib plots the progression of the disease states over time.

## The SEIR Model

The simulation follows the progression:

\[
S \rightarrow E \rightarrow I \rightarrow R
\]

Transmission occurs when a susceptible individual shares a location with an infectious individual and a transmission event succeeds. Newly exposed individuals must complete the latent period before becoming infectious.

Recovered individuals remain immune for the duration of the simulation. Reinfection, disease-induced mortality and waning immunity are not modelled.

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Entry point; runs the simulation and reports results. |
| `config.py` | Stores simulation parameters and derived values. |
| `clock.py` | Tracks simulated time. |
| `disease.py` | Defines the disease-state enumeration. |
| `person.py` | Defines individual agents and their disease-related attributes. |
| `location.py` | Defines locations, homes and workplace types. |
| `initialise.py` | Creates the population and assigns locations and initial disease states. |
| `simulation.py` | Implements transmission, disease progression, recovery and statistical recording. |
| `visualisation.py` | Plots the recorded simulation results. |

## Requirements

- Python 3
- Matplotlib
- `names` package

Install the external dependencies with:

```bash
pip install matplotlib names
```

## Running the Simulation

Run the entry point from the project directory:

```bash
python main.py
```

The program runs the simulation using the parameters defined in `config.py`, prints summary statistics and displays a plot of the disease progression.

## Configuration

Simulation parameters are defined in `config.py`. These include:

- Population size and simulation duration.
- Initial numbers of infected and recovered individuals.
- Transmission probability.
- Expected infection-period parameter and recovery probabilities.
- Maximum infection-period threshold.
- Latent period before exposed individuals become infectious.

Changing these values allows different model configurations to be explored without modifying the core simulation logic.

## Modelling Assumptions and Limitations

This project is an educational simulation rather than a validated epidemiological forecasting tool.

- Each infectious–susceptible pair at the same location receives an independent transmission attempt during each simulated hour.
- Individuals are assigned to homes and workplaces, and their locations depend on workplace opening hours.
- The latent period is fixed rather than drawn from a probability distribution.
- Recovery is stochastic rather than guaranteed at a single infection duration.
- Recovered individuals remain immune throughout the simulation.
- The model does not account for age-dependent transmission, asymptomatic infection, vaccination, mortality or real-world mobility patterns.
- The simulation parameters have not been calibrated against real-world epidemic data.

These simplifications make the model manageable to implement and analyse, but they limit how closely its results represent real epidemics.

## Learning Objectives

This project was developed to practise:

- Object-oriented programming and inheritance.
- Modelling interacting agents and locations.
- Implementing stochastic processes.
- Managing discrete-time simulations.
- Recording and analysing time-series data.
- Visualising simulation results.

## Future Extensions

Potential extensions include more detailed contact patterns, multiple workplace schedules, intervention modelling and statistical comparisons across repeated simulation runs.

These are possible directions for further development rather than features currently implemented.
