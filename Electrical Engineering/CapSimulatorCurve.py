# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np

# Prompt the user for the initial charge and capacitance of the capacitor
charge = float(input("Enter the initial charge of the capacitor (C): "))
capacitance = float(input("Enter the capacitance of the capacitor (F): "))

# Set the time step and total simulation time
dt = 0.01
total_time = 10

# Prompt the user for the resistance and the applied voltage
resistance = float(input("Enter the resistance of the circuit (Ohms): "))
voltage = float(input("Enter the applied voltage (V): "))

# Create arrays to store the charge and time value
charges = []
times = []

# Simulate the charging and discharging of the capacitor
for time in np.arange(0, total_time, dt):
    # Calculate the current flowing through the capacitor
    current = (voltage - (charge / capacitance)) / resistance

    # Calculate the change in charge of the capacitor
    dq = current * dt

    # Update the charge of the capacitor
    charge += dq

    # Store the current charge and time
    charges.append(charge)
    times.append(time)

# Plot the charging and discharging curves
plt.plot(times, charges)
plt.xlabel("Time (s)")
plt.ylabel("Charge (C)")
plt.show()
