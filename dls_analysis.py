import numpy as np
import matplotlib.pyplot as plt

# Sample DLS particle size data (nm)
particle_size = np.array([10, 20, 30, 40, 50, 60])
intensity = np.array([5, 15, 40, 25, 10, 5])

plt.figure()
plt.plot(particle_size, intensity, marker='o')

plt.title("DLS Particle Size Distribution")
plt.xlabel("Particle Size (nm)")
plt.ylabel("Intensity (%)")

plt.grid(True)
plt.show()
