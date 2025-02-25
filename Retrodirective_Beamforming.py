import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
f_r = 2.45e9  # Frequency of pilot signal (Hz)
f_t = 5.8e9  # Frequency of transmission signal (Hz)
lambda_r = c / f_r  # Wavelength of pilot signal (m)
lambda_t = c / f_t  # Wavelength of transmission signal (m)

# Antenna Spacing (D is same for both, but expressed in different wavelengths)
d = 1.3 * lambda_t  # Common physical spacing in meters
spacing_dipole = d / lambda_r  # Expressed in terms of pilot signal wavelength
spacing_patch = d / lambda_t  # Expressed in terms of transmission signal wavelength

# Number of elements
num_antennas = 4

# Incident angles of pilot signal (degrees)
theta_incidents = [1, 2, 5]  # Received from 1, 2, and 5 degrees

# Data storage
results = []

for theta_incident in theta_incidents:
    # Compute phase at each dipole antenna
    dipole_phase = np.array([(2 * np.pi * spacing_dipole) * np.sin(np.radians(theta_incident)) * i for i in range(num_antennas)])
    
    # Compute conjugate phase for each patch antenna based on frequency ratio
    patch_phase = - (f_t / f_r) * dipole_phase
    
    # Normalize phases to [-pi, pi]
    patch_phase = np.angle(np.exp(1j * patch_phase))
    
    # Store results
    for i in range(num_antennas):
        results.append([theta_incident, i+1, np.degrees(dipole_phase[i]), np.degrees(patch_phase[i])])

# Convert to DataFrame
df = pd.DataFrame(results, columns=["Incident Angle (deg)", "Antenna Index", "Received Phase (deg)", "Conjugate Phase (deg)"])

# Display table
print(df.to_string(index=False))

# Beamforming pattern calculation for 5-degree incident signal
theta = np.linspace(-30, 30, 1000)  # Observation angles
e_field = np.zeros_like(theta, dtype=complex)

# Extract conjugate phase for 5-degree incident signal
subset_5deg = df[df["Incident Angle (deg)"] == 5]["Conjugate Phase (deg)"].values
patch_phase_radians = np.radians(subset_5deg)

for i in range(num_antennas):
    e_field += np.exp(1j * ((2 * np.pi * spacing_patch) * np.sin(np.radians(theta)) * i + patch_phase_radians[i]))

# Normalize and convert to dB
beam_pattern = 20 * np.log10(np.abs(e_field) / np.max(np.abs(e_field)))

# Plot beam pattern
plt.figure(figsize=(8, 5))
plt.plot(theta, beam_pattern, label='Beam Pattern for 5° Incident Angle')
plt.axvline(x=5, color='r', linestyle='dashed', label='Expected Beam Direction (5°)')
plt.xlabel("Angle (degrees)")
plt.ylabel("Normalized Gain (dB)")
plt.title("Beam Pattern for 5° Incident Angle")
plt.legend()
plt.grid()
plt.show()
