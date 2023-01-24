import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk


# create a class to represent the GUI
class CapacitorCurve:
    def __init__(self, master):
        self.master = master
        master.title("Capacitor Curve")

        # create a label for the capacitance entry field
        self.label = Label(master, text="Enter capacitance (microfarads):")
        self.label.pack()

        # create an entry field for the capacitance
        self.capacitance_entry = Entry(master)
        self.capacitance_entry.pack()

        # create a button to plot the curve
        self.plot_button = ttk.Button(master, text="Plot Curve", command=self.plot)
        self.plot_button.pack()

    # function to plot the curve
    def plot(self):
        # get the capacitance value entered by the user
        capacitance = float(self.capacitance_entry.get())
        # create an array of time values
        time = np.linspace(0, 10, 1000)
        # calculate the voltage values based on the capacitance and time
        voltage = np.exp(-time / (capacitance * 0.001))

        # create the plot using Matplotlib
        plt.plot(time, voltage)
        plt.xlabel("Time (s)")
        plt.ylabel("Voltage (V)")
        plt.title("Capacitor Charging/Discharging Curve")
        plt.grid(True)
        plt.show()


# create the GUI
root = Tk()
my_gui = CapacitorCurve(root)
root.mainloop()
