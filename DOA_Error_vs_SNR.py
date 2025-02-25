import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
f = 2.45e9  # Frequency (Hz)
lambda_wave = c / f  # Wavelength (m)
antenna_gain_dBi = 14  # Gain of 4x4 antenna array in dBi

# Baselines (in meters)
baselines = [1, 2.5, 5]

# Angle of Arrival (degrees)
theta_incident = 5  # Fixed at 5 degrees

# SNR values in dB
SNR_dB = np.linspace(10, 60, 10)  # From 10 dB to 60 dB
SNR_linear = 10**(SNR_dB / 10)  # Convert SNR from dB to linear scale

# Simulating standard deviation of phase difference
np.random.seed(42)  # For reproducibility

# Dictionary to store AOA errors for different baselines
error_aoa_results = {}

for d in baselines:
    error_aoa = []
    
    for snr in SNR_linear:
        # Standard deviation of phase difference approximation
        sigma_phi = 1 / np.sqrt(snr)  # Simplified noise model
        
        # Compute AOA error using Equation (1): Δθ = sin⁻¹( λσφ / 2πd )
        error_theta = np.degrees(np.arcsin((lambda_wave * sigma_phi) / (2 * np.pi * d)))
        error_aoa.append(error_theta)
    
    # Store results
    error_aoa_results[d] = error_aoa

# Plot results
plt.figure(figsize=(8, 5))
for d in baselines:
    plt.plot(SNR_dB, error_aoa_results[d], marker='o', label=f'Baseline = {d}m')

plt.xlabel('SNR (dB)')
plt.ylabel('Error of AOA (degrees)')
plt.title('Error of Angle of Arrival vs SNR for Different Baselines')
plt.legend()
plt.grid()
plt.show()
