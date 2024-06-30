import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.widgets import Button

# Time parameters
dt = 0.1  # Reduced time step for higher resolution
T = 10
time = np.arange(0, T, dt)

# Initial conditions
q0 = -4.5
q_dot0 = 3

# Arrays to store position, velocity, and control input
q = np.zeros_like(time)
q_dot = np.zeros_like(time)
u = np.zeros_like(time)

# Set initial conditions
q[0] = q0
q_dot[0] = q_dot0

threshold = 0.1

def calculate_control(q, q_dot):
    if abs(q) < threshold and abs(q_dot) < threshold:
        return 0
    elif (q_dot < 0 and q < 0.5 * q_dot ** 2) or (q_dot >= 0 and q < -0.5 * q_dot ** 2):
        return 1
    else:
        return -1

# Animation control variable
anim_running = True

def update(i):
    global q, q_dot, u, anim_running
    
    if not anim_running:
        return line_q, line_q_dot
    
    if i == 0:
        q[i] = q0
        q_dot[i] = q_dot0
    else:
        # Calculate control input
        u[i] = calculate_control(q[i-1], q_dot[i-1])
        
        # Update velocity and position using the control input
        q_dot[i] = q_dot[i-1] + u[i] * dt
        q[i] = q[i-1] + q_dot[i-1] * dt
    
    # Update plot data
    line_q.set_data(time[:i+1], q[:i+1])
    line_q_dot.set_data(time[:i+1], q_dot[:i+1])
    
    return line_q, line_q_dot

# Pause and Resume button functions
def pause_animation(event):
    global anim_running
    anim_running = False

def resume_animation(event):
    global anim_running
    anim_running = True

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Initialize lines for plots
line_q, = ax1.plot([], [], label='Position (q)')
ax1.axhline(0, color='gray', linestyle='--')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Position (q)')
ax1.legend()
ax1.grid()

line_q_dot, = ax2.plot([], [], label='Velocity (q_dot)')
ax2.axhline(0, color='gray', linestyle='--')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (q_dot)')
ax2.legend()
ax2.grid()

# Set initial y-axis limits
ax1.set_ylim(-5, 5)
ax2.set_ylim(-5, 5)

# Set initial x-axis limits
ax1.set_xlim(0, T)
ax2.set_xlim(0, T)

# Create pause and resume buttons
pause_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
pause_button = Button(pause_ax, 'Pause')
pause_button.on_clicked(pause_animation)

resume_ax = plt.axes([0.9, 0.025, 0.1, 0.04])
resume_button = Button(resume_ax, 'Resume')
resume_button.on_clicked(resume_animation)

# Set up the animation
ani = FuncAnimation(fig, update, frames=len(time), blit=True, interval=dt * 1000, repeat=False)

# Save animation as GIF
ani.save('control_system_animation.gif', writer='pillow', fps=10)  # Adjust fps as needed

plt.tight_layout()
plt.show()

