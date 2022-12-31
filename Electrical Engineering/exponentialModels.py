import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def visualize_exponential(base, exponent, x_range):
    # Calculate the y values for the given x range
    y_values = [base ** x for x in x_range]
    
    # Create the plot
    plt.plot(x_range, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Exponential Function: y = {base}^x')
    
    # Show the plot
    plt.show()

# Create the root window
root = tk.Tk()
root.title('Exponential Visualization')

# Create the form frame
form_frame = ttk.Frame(root, padding=10)
form_frame.grid()

# Create the base entry widget
base_label = ttk.Label(form_frame, text='Base:')
base_label.grid(row=0, column=0)
base_entry = ttk.Entry(form_frame)
base_entry.grid(row=0, column=1)

# Create the exponent entry widget
exponent_label = ttk.Label(form_frame, text='Exponent:')
exponent_label.grid(row=1, column=0)
exponent_entry = ttk.Entry(form_frame)
exponent_entry.grid(row=1, column=1)

# Create the submit button
submit_button = ttk.Button(form_frame, text='Submit', command=lambda: visualize_exponential(
    int(base_entry.get()),
    int(exponent_entry.get()),
    range(10)
))
submit_button.grid(row=2, column=1)

# Run the main loop
root.mainloop()
