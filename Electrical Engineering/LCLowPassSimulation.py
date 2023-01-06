import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from scipy import signal

# Create the main window
root = tk.Tk()

# Create the widgets for the input form
l_label = tk.Label(root, text="Inductance (H):")
l_entry = tk.Entry(root)
c_label = tk.Label(root, text="Capacitance (F):")
c_entry = tk.Entry(root)

# Create the button to calculate the response
calc_button = ttk.Button(root, text="Calculate")


# Define the function to be called when the button is clicked
def calculate():
    # Get the values entered by the user
    l = float(l_entry.get())
    c = float(c_entry.get())

    # Calculate the transfer function of the filter
    s = signal.lti([], [l * c, 1], 1)

    # Calculate the frequency response of the filter
    w, mag, phase = s.bode()

    # Plot the frequency response
    plt.figure()
    plt.semilogx(w, mag)
    plt.xlabel("Frequency (rad/s)")
    plt.ylabel("Magnitude (dB)")
    plt.title("Frequency Response of LC Low Pass Filter")
    plt.grid()
    plt.show()


# Set the button to call the calculate function when clicked
calc_button.config(command=calculate)

# Place the widgets in the window
l_label.grid(row=0, column=0)
l_entry.grid(row=0, column=1)
c_label.grid(row=1, column=0)
c_entry.grid(row=1, column=1)
calc_button.grid(row=2, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
