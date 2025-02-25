import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
f_r = 2.45e9  # Frequency of pilot signal (Hz)
f_t = 5.8e9  # Frequency of transmission signal (Hz)
lambda_r = c / f_r  # Wavelength of pilot signal (m)
lambda_t = c / f_t  # Wavelength of transmission signal (m)

# Antenna Spacing
spacing_patch = 1.3 * lambda_t  # Patch antenna spacing (m)
num_antennas = 4  # Number of elements

theta_incident = 5  # Angle of Arrival (degrees)

# Antenna Deformation (Antenna 2 and Antenna 3 shifted by 0.5 lambda_t)
deformation_shift = 0.5 * lambda_t

# Compute initial received phase at dipoles
dipole_phase = np.array([(2 * np.pi * spacing_patch / lambda_r) * np.sin(np.radians(theta_incident)) * i for i in range(num_antennas)])

# Introduce deformation at Antenna 2 and Antenna 3
dipole_phase_deformed = dipole_phase.copy()
dipole_phase_deformed[1] += (2 * np.pi * deformation_shift / lambda_r)  # Equation 2 correction
dipole_phase_deformed[2] += (2 * np.pi * deformation_shift / lambda_r)  # Equation 2 correction

# Compute conjugate phases for beam steering (without correction uses initial values)
patch_phase_without_correction = - (f_t / f_r) * dipole_phase_deformed  # Without correction: uses original dipole phase values
patch_phase_with_correction = - (f_t / f_r) * dipole_phase  # With correction: uses updated dipole phase values

# Normalize phases to [-pi, pi]
patch_phase_without_correction = np.angle(np.exp(1j * patch_phase_without_correction))
patch_phase_with_correction = np.angle(np.exp(1j * patch_phase_with_correction))

# Beamforming pattern calculation
theta = np.linspace(-30, 30, 1000)  # Observation angles
e_field_without_correction = np.zeros_like(theta, dtype=complex)
e_field_with_correction = np.zeros_like(theta, dtype=complex)

for i in range(num_antennas):
    e_field_without_correction += np.exp(1j * ((2 * np.pi * spacing_patch / lambda_t) * np.sin(np.radians(theta)) * i + patch_phase_without_correction[i]))
    e_field_with_correction += np.exp(1j * ((2 * np.pi * spacing_patch / lambda_t) * np.sin(np.radians(theta)) * i + patch_phase_with_correction[i]))

# Normalize and convert to dB
beam_pattern_without_correction = 20 * np.log10(np.abs(e_field_without_correction) / np.max(np.abs(e_field_without_correction)))
beam_pattern_with_correction = 20 * np.log10(np.abs(e_field_with_correction) / np.max(np.abs(e_field_with_correction)))

# Plot beam patterns
plt.figure(figsize=(8, 5))
plt.plot(theta, beam_pattern_without_correction, label='Without Correction', linestyle='dashed')
plt.plot(theta, beam_pattern_with_correction, label='With Correction', linestyle='solid')
plt.axvline(x=5, color='r', linestyle='dashed', label='Expected Beam Direction (5°)')
plt.xlabel("Angle (degrees)")
plt.ylabel("Normalized Gain (dB)")
plt.title("Antenna Deformation Correction Using Retrodirective Method")
plt.legend()
plt.grid()
plt.show()

# Print phase values
print("Received Phase (Without Correction):", np.degrees(dipole_phase_deformed))
print("Received Phase (With Correction):", np.degrees(dipole_phase))
print("Conjugate Phase (Without Correction):", np.degrees(patch_phase_without_correction))
print("Conjugate Phase (With Correction):", np.degrees(patch_phase_with_correction))
