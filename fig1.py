import numpy as np
import matplotlib.pyplot as plt

# Define the range for omega
omega_min = -np.pi
omega_max = np.pi
num_points = 1000  # Number of points for omega

# Generate values for omega
omega = np.linspace(omega_min, omega_max, num_points)

# Calculate the function values
y = 2 * np.abs(np.cos(omega/2))

# Plot
plt.plot(omega, y)
plt.xlabel(r'$\omega$')
plt.ylabel(r'$2|\cos(\frac{\omega}{2})|$')
plt.grid(True)
plt.savefig('../figs/fig1.png')
