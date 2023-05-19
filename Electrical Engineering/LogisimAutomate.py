import os
import subprocess
import time
import tkinter as tk
from tkinter import filedialog


class LogisimController:
    # Create the GUI window
    def __init__(self):
        self.logisim_path = ''
        self.circuit_path = ''

    # Browse for the circuit file
    def browse_file(self):
        self.circuit_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select Logisim circuit file",
            filetypes=(("Logisim circuit files", "*.circ"), ("all files", "*.*"))
        )
        self.filepath_var.set(self.circuit_path)

    # Run the simulation
    def run_simulation(self):
        # Start Logisim
        subprocess.Popen(['java', '-jar', self.logisim_path])

        # Wait for Logisim to start
        time.sleep(5)

        # Use PyAutoGUI to automate Logisim
        import pyautogui

        # Open the selected circuit file
        pyautogui.hotkey('ctrl', 'o')
        time.sleep(2)
        pyautogui.write(self.circuit_path, interval=0.1)
        pyautogui.press('enter')

        # Run the simulation
        pyautogui.hotkey('ctrl', 'r')

    # Create the GUI
    def create_gui(self):
        root = tk.Tk()
        root.title("Logisim Controller")

        # Logisim path label and browse button
        logisim_label = tk.Label(root, text="Logisim path:")
        logisim_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.logisim_path_entry = tk.Entry(root, width=50)
        self.logisim_path_entry.grid(row=0, column=1, padx=5, pady=5)
        logisim_browse_button = tk.Button(root, text="Browse", command=self.browse_logisim)
        logisim_browse_button.grid(row=0, column=2, padx=5, pady=5)

        # Circuit path label and browse button
        circuit_label = tk.Label(root, text="Circuit path:")
        circuit_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.filepath_var = tk.StringVar()
        circuit_path_entry = tk.Entry(root, width=50, textvariable=self.filepath_var)
        circuit_path_entry.grid(row=1, column=1, padx=5, pady=5)
        circuit_browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        circuit_browse_button.grid(row=1, column=2, padx=5, pady=5)

        # Run button
        run_button = tk.Button(root, text="Run Simulation", command=self.run_simulation)
        run_button.grid(row=2, column=1, padx=5, pady=5)

        root.mainloop()

    # Browse for the Logisim executable file
    def browse_logisim(self):
        self.logisim_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select Logisim executable file",
            filetypes=(("Logisim executable files", "*.jar"), ("all files", "*.*"))
        )
        self.logisim_path_entry.delete(0, tk.END)
        self.logisim_path_entry.insert(0, self.logisim_path)


# Run the program
if __name__ == "__main__":
    logisim_controller = LogisimController()
    logisim_controller.create_gui()

