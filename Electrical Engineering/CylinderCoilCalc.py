import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from scipy.constants import mu_0


# main window class for the Cylindrical Coil Calculator program
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cylindrical Coil Calculator")
        self.setGeometry(100, 100, 400, 250)

        # Create labels and input fields
        self.label_radius = QLabel("Radius (m):", self)
        self.label_radius.setGeometry(20, 20, 100, 20)
        self.input_radius = QLineEdit(self)
        self.input_radius.setGeometry(140, 20, 100, 20)

        self.label_length = QLabel("Length (m):", self)
        self.label_length.setGeometry(20, 50, 100, 20)
        self.input_length = QLineEdit(self)
        self.input_length.setGeometry(140, 50, 100, 20)

        # Create calculate button
        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.setGeometry(20, 80, 80, 30)
        self.calculate_button.clicked.connect(self.calculate)

        # Create plot button
        self.plot_button = QPushButton("Plot", self)
        self.plot_button.setGeometry(120, 80, 80, 30)
        self.plot_button.clicked.connect(self.plot)

        # Create status label
        self.status_label = QLabel("", self)
        self.status_label.setGeometry(20, 120, 300, 20)

    # Calculate magnetic field
    def calculate(self):
        try:
            radius = float(self.input_radius.text())
            length = float(self.input_length.text())

            # Calculate magnetic field and other values
            num_turns = 1  # Number of turns, assuming a single coil
            current = 1  # Current in amperes
            N = num_turns * current
            B = (mu_0 * N * radius ** 2) / (2 * (radius ** 2 + length ** 2) ** (3 / 2))

            self.status_label.setText(f"Magnetic Field: {B:.6f} T")

        except ValueError:
            self.status_label.setText("Invalid input. Please enter valid numbers.")

    # Plot magnetic field
    def plot(self):
        try:
            radius = float(self.input_radius.text())
            length = float(self.input_length.text())

            # Generate plot data
            z = np.linspace(-length / 2, length / 2, 100)
            b_field = ((mu_0 * radius ** 2) / (2 * (radius ** 2 + z ** 2) ** (3 / 2)))

            # Plot magnetic field
            plt.plot(z, b_field)
            plt.xlabel('Z-axis (m)')
            plt.ylabel('Magnetic Field (T)')
            plt.title('Magnetic Field along Z-axis')
            plt.grid(True)
            plt.show()

        except ValueError:
            self.status_label.setText("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
