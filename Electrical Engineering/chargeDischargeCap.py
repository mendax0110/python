import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk


class CapacitorCurve:
    def __init__(self, master):
        self.master = master
        master.title("Capacitor Curve")

        self.label = Label(master, text="Enter capacitance (microfarads):")
        self.label.pack()

        self.capacitance_entry = Entry(master)
        self.capacitance_entry.pack()

        self.plot_button = ttk.Button(master, text="Plot Curve", command=self.plot)
        self.plot_button.pack()

    def plot(self):
        capacitance = float(self.capacitance_entry.get())
        time = np.linspace(0, 10, 1000)
        voltage = np.exp(-time / (capacitance * 0.001))

        plt.plot(time, voltage)
        plt.xlabel("Time (s)")
        plt.ylabel("Voltage (V)")
        plt.title("Capacitor Charging/Discharging Curve")
        plt.show()


root = Tk()
my_gui = CapacitorCurve(root)
root.mainloop()
