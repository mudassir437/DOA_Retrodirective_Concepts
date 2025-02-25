# Direction of Arrival (DOA) and Retrodirective Beamforming Concepts

This repository contains **Python scripts** that demonstrate key **Direction of Arrival (DOA) estimation** and **Retrodirective Beamforming** techniques, relevant for **wireless power transmission in Space-Based Solar Power (SBSP) systems**. These scripts conceptually illustrate methods used in my **MSc and PhD research** to improve **AOA accuracy** and address **synchronization issues in phased arrays**.

## Overview of the Scripts

- **DOA Error vs. SNR Script**\
  Analyzes **AOA estimation accuracy** by evaluating **error vs. SNR** for different baselines.

- **DOA Least Squares Fitting Script**\
  Predicts **SNR values from experimental data**, which can be used in **real solar power satellite applications**.

- **Retrodirective Beamforming Script**\
  Models a **1×4 patch antenna subarray**, applying **phase conjugation** for autonomous signal redirection.

- **Antenna Deformation Compensation Script**\
  Compensates for **beam misalignment** caused by structural deformations in antennas.

These scripts **are not exact research implementations**, but **conceptual demonstrations** of signal processing techniques used in **SBSP applications**. They helped establish a foundation before conducting **CST simulations** and **real anechoic chamber experiments** with **LabVIEW/GNU Radio-based software-defined radios**, validating these techniques for **wireless power transmission**.

## Full Commentary

For a detailed explanation of the approach and methodology, see [COMMENTARY.md](COMMENTARY.md).

## How to Use the Scripts

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/DOA_Retrodirective_Concepts.git
   ```
2. Install dependencies:
   ```bash
   pip install numpy matplotlib
   ```
3. Run a script:
   ```bash
   python script_name.py
   ```

