# Bang Bang Control Policy - Double Integrator System

This is a solution to the minimum time problem for the double integrator with input constraints. A Bang-bang controller was implemented as an optimal solution. It is based on example 7.2 in Underactuated Robotics. The system is governed by the following dynamics and control logic:

## Dynamics

The system dynamics are described by (note initial conditions were chosen such that c=0):
- Position (q) with initial condition q0 = -4.5
- Velocity (q_dot) with initial condition q_dot0 = 3

The system evolves over time (T = 10 seconds) with a time step dt = 0.1 seconds for higher resolution.

## Control Logic

The control input (u) is determined by the function `calculate_control(q, q_dot)`, which follows these rules:
- If the absolute values of q and q_dot are less than a threshold (threshold = 0.1), then u = 0.
- Otherwise, if q_dot < 0 and q < 0.5 * q_dot ** 2, or q_dot >= 0 and q < -0.5 * q_dot ** 2, then u = 1.
- Otherwise, u = -1.

**Note:** The threshold parameter (`threshold = 0.1`) determines when the control input u is set to 0 based on the absolute values of position (q) and velocity (q_dot).

## Visualization

The system's position (q) and velocity (q_dot) are visualized over time using Matplotlib. The animation shows how the position and velocity evolve under the influence of the control input u.

## Usage

To run the simulation and visualize the results:
1. Make sure you have Python and Matplotlib installed.
2. Run the script `control_system_simulation.py`.
3. Observe the animated plot that displays the evolution of position and velocity over time.

## Files

- `control_system_simulation.py`: Main Python script containing the simulation and visualization code.
- `README.md`: This file, providing an overview of the project.

## Note

Adjust the initial conditions (q0, q_dot0), time parameters (T, dt), and control logic (threshold, `calculate_control` function) as needed for different scenarios or experiments.

Feel free to explore and modify the code to suit your specific requirements or extend it for more complex control system simulations.
