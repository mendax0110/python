import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

# Define the function for calculating and plotting the filter's frequency response
def calculate_and_plot(R, C):
    # Calculate the filter's corner frequency
    fc = 1 / (2 * np.pi * R * C)

    # Define the frequency range for the plot
    f = np.logspace(0, 9, 1000)

    # Calculate the filter's transfer function
    H = 1 / (1 + (1j * f) / fc)

    # Plot the frequency response
    plt.semilogx(f, 20 * np.log10(np.abs(H)))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain (dB)")
    plt.show()

# Create the main window
root = Tk()
root.title("RC Filter Calculator")

# Create the input fields for resistance and capacitance
resistance_label = Label(root, text="Resistance (ohms):")
resistance_entry = Entry(root)
capacitance_label = Label(root, text="Capacitance (farads):")
capacitance_entry = Entry(root)

# Create the "Calculate" button
button = Button(root, text="Calculate", command=lambda: calculate_and_plot(float(resistance_entry.get()), float(capacitance_entry.get())))

# Place the input fields and button in the window
resistance_label.grid(row=0, column=0)
resistance_entry.grid(row=0, column=1)
capacitance_label.grid(row=1, column=0)
capacitance_entry.grid(row=1, column=1)
button.grid(row=2, column=0, columnspan=2)

# Start the main loop
root.mainloop()

