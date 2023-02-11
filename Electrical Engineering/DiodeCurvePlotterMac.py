import matplotlib
import numpy as np
import sys

if sys.platform == "darwin":
    matplotlib.use("MacOSX")
else:
    matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk


class DiodeCurvePlotter:
    def __init__(self, master):
        self.master = master
        master.title("Diode Curve Plotter")

        # create figure and canvas to display plot
        self.figure = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.figure, master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)

        # create entry for diode forward voltage
        self.vf_label = tk.Label(master, text="Diode Forward Voltage (Vf):")
        self.vf_label.pack()
        self.vf_entry = tk.Entry(master)
        self.vf_entry.pack()

        # create entry for diode reverse saturation current
        self.is_label = tk.Label(master, text="Diode Reverse Saturation Current (Is):")
        self.is_label.pack()
        self.is_entry = tk.Entry(master)
        self.is_entry.pack()

        # create submit button
        self.plot_button = tk.Button(master, text="Plot", command=self.plot_curve)
        self.plot_button.pack()

    def plot_curve(self):
        # get values from entries
        vf = float(self.vf_entry.get())
        is_ = float(self.is_entry.get())

        # clear previous plot
        self.figure.clear()

        # calculate and plot diode curve
        v = [v for v in range(-10, 10)]
        i = [is_ * (np.exp(vv / vf) - 1) for vv in v]
        plt.plot(v, i)

        # update canvas
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = DiodeCurvePlotter(root)
    root.mainloop()
