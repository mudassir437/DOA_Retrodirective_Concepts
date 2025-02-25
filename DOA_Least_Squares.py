import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the least squares fitting function
def least_squares_fit(x, a, b):
    return a / np.sqrt(x) + b

# Example data (SNR values and corresponding experimental error of AOA)
SNR_values = np.linspace(10, 60, 10)  # Example SNR values (dB)
experimental_data = np.array([0.01, 0.008, 0.007, 0.0065, 0.006, 0.0058, 0.0055, 0.0052, 0.005, 0.0048])

# Apply least squares fitting
popt, _ = curve_fit(least_squares_fit, SNR_values, experimental_data)
fitted_data = least_squares_fit(SNR_values, *popt)

# Plot experimental vs fitted data
plt.figure(figsize=(8, 5))
plt.scatter(SNR_values, experimental_data, label='Experimental Data', color='red')
plt.plot(SNR_values, fitted_data, label='Least Squares Fit', linestyle='solid')
plt.xlabel('SNR (dB)')
plt.ylabel('Error of AOA (degrees)')
plt.title('Least Squares Fit of AOA Error vs SNR')
plt.legend()
plt.grid()
plt.show()
