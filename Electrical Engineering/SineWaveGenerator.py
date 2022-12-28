import tkinter as tk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def sine_wave(frequency, num_terms):
  # Generate the x values
  x = np.linspace(0, 2*np.pi, 1000)

  # Generate the y values
  y = 0
  for n in range(num_terms):
    y += np.sin((2*n+1)*frequency*x)/(2*n+1)

  return x, y

class SineWaveGenerator(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    tk.Tk.wm_title(self, "Sine Wave Generator")

    # Create a frame for the input fields
    input_frame = tk.Frame(self)
    input_frame.pack(side="top", fill="x")

    # Create a label and entry field for the frequency
    frequency_label = tk.Label(input_frame, text="Frequency:")
    frequency_label.pack(side="left")
    self.frequency_entry = tk.Entry(input_frame)
    self.frequency_entry.pack(side="left")

    # Create a label and entry field for the number of terms
    num_terms_label = tk.Label(input_frame, text="# of terms:")
    num_terms_label.pack(side="left")
    self.num_terms_entry = tk.Entry(input_frame)
    self.num_terms_entry.pack(side="left")

    # Create a button to generate the sine wave
    generate_button = tk.Button(input_frame, text="Generate", command=self.generate_sine_wave)
    generate_button.pack(side="left")

    # Create a frame to hold the plot
    plot_frame = tk.Frame(self)
    plot_frame.pack(side="bottom", fill="both", expand=True)

    # Create a figure and canvas to display the plot
    self.figure = plt.Figure(figsize=(5,5))
    self.canvas = FigureCanvasTkAgg(self.figure, plot_frame)
    self.canvas.draw()
    self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

    # Add a toolbar for navigating the plot
    self.toolbar = NavigationToolbar2Tk(self.canvas, plot_frame)
    self.toolbar.update()
    self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

  def generate_sine_wave(self):
    # Get the input values from the entry fields
    frequency = float(self.frequency_entry.get())
    num_terms = int(self.num_terms_entry.get())

    # Generate the sine wave
    x, y = sine_wave(frequency, num_terms)

    # Clear the figure
    self.figure.clear()

    # Plot the sine wave
    self.figure.add_subplot(111).plot(x, y)

    # Redraw the canvas
    self.canvas.draw()

if __name__ == "__main__":
    app = SineWaveGenerator()
    app.mainloop()



    
