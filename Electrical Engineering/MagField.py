import sys
import math
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class FieldCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Field Calculator")
        self.layout = QVBoxLayout()

        self.label_q = QLabel("Enter charge (in C):")
        self.input_q = QLineEdit()
        self.layout.addWidget(self.label_q)
        self.layout.addWidget(self.input_q)

        self.label_d = QLabel("Enter distance (in m):")
        self.input_d = QLineEdit()
        self.layout.addWidget(self.label_d)
        self.layout.addWidget(self.input_d)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        self.layout.addWidget(self.calculate_button)

        self.setLayout(self.layout)

    def calculate(self):
        q = float(self.input_q.text())
        d = float(self.input_d.text())

        # Calculate electric field
        k = 8.99 * 10 ** 9  # Coulomb's constant
        electric_field = k * q / d ** 2

        # Calculate magnetic field
        mu0 = 4 * math.pi * 10 ** -7  # Permeability of free space
        magnetic_field = mu0 * q / (2 * math.pi * d)

        # Plot field lines
        theta = [i for i in range(361)]
        x_electric = [d * math.cos(math.radians(t)) for t in theta]
        y_electric = [electric_field * math.sin(math.radians(t)) for t in theta]
        x_magnetic = [d * math.cos(math.radians(t)) for t in theta]
        y_magnetic = [magnetic_field * math.sin(math.radians(t)) for t in theta]

        plt.plot(x_electric, y_electric, label="Electric Field")
        plt.plot(x_magnetic, y_magnetic, label="Magnetic Field")
        plt.legend()
        plt.xlabel("Distance (m)")
        plt.ylabel("Field Strength (T)")
        plt.title("Electric and Magnetic Field Lines")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FieldCalculator()
    window.show()
    sys.exit(app.exec_())
