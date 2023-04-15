import sys
import os
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt


# Create a main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("PyLTspice")

        # Set the window size
        self.setGeometry(100, 100, 800, 600)

        # Add a label
        label = QLabel("Welcome to PyLTspice!", self)
        label.move(50, 50)

        # Add a button to load the circuit file
        load_button = QPushButton("Load Circuit", self)
        load_button.move(50, 100)
        load_button.clicked.connect(self.load_circuit)

        # Add a button to save the circuit file
        save_button = QPushButton("Save Circuit", self)
        save_button.move(50, 150)
        save_button.clicked.connect(self.save_circuit)

        # Add a button to edit the circuit file
        edit_button = QPushButton("Edit Circuit", self)
        edit_button.move(50, 200)
        edit_button.clicked.connect(self.edit_circuit)

        # Add a button to show the voltage and current graph
        graph_button = QPushButton("Show Graph", self)
        graph_button.move(50, 250)
        graph_button.clicked.connect(self.show_graph)

        # Initialize file path
        self.file_path = None

    # load the circuit file
    def load_circuit(self):
        # Define file dialog to let the user select a circuit file
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("LTspice Files (*.asc *.net *.cir *.sp)")

        if file_dialog.exec_():
            self.file_path = file_dialog.selectedFiles()[0]

            # Load the circuit file
            lts = LTSpiceRawRead(self.file_path)

            # Simulate the circuit
            lts.run()

            # Get the voltage and current traces
            self.time, self.voltage = lts.get_trace("V(out)")
            self.time, self.current = lts.get_trace("I(R1)")

            # Update label to display loaded file name
            file_name = os.path.basename(self.file_path)
            self.label.setText(f"Loaded file: {file_name}")

    # Save the circuit file
    def save_circuit(self):
        if self.file_path is not None:
            # Write the current circuit to the original file
            with open(self.file_path, "w") as f:
                f.write("Example circuit\n")
                f.write("* Some comment\n")
                f.write("R1 in out 1k\n")
                f.write("V1 in 0 1\n")
                f.write(".end\n")

            # Update label to display saved file name
            file_name = os.path.basename(self.file_path)
            self.label.setText(f"Saved file: {file_name}")

    # Open the circuit file in a text editor
    def edit_circuit(self):
        if self.file_path is not None:
            # Open the circuit file in a text editor
            os.system(f"start notepad.exe {self.file_path}")

    # Plot the voltage and current traces
    def show_graph(self):
        if self.file_path is not None:
            # Plot the voltage and current traces
            plt.plot(self.time, self.voltage, label="Voltage")
            plt.plot(self.time, self.current, label="Current")
            plt.xlabel("Time (s)")
            plt.ylabel("Voltage (V) / Current (A)")
            plt.legend("upper right")
            plt.show()

            # Update label to display graphed file name
            file_name = os.path.basename(self.file_path)
            self.label.setText(f"Graphed file: {file_name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
