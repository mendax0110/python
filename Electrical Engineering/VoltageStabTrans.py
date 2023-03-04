from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main window
        self.setWindowTitle("Collector-Base Voltage Graph")
        self.setGeometry(100, 100, 800, 600)

        # Create the plot
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Collector-Base Voltage Graph")
        self.ax.set_xlabel("Voltage (V)")
        self.ax.set_ylabel("Current (mA)")

        # Create the input fields
        self.collector_label = QLabel("Collector Voltage:", self)
        self.collector_label.move(50, 50)
        self.collector_input = QLineEdit(self)
        self.collector_input.move(150, 50)
        self.base_label = QLabel("Base Voltage:", self)
        self.base_label.move(50, 80)
        self.base_input = QLineEdit(self)
        self.base_input.move(150, 80)

        # Create the calculate button
        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.move(150, 120)
        self.calculate_button.clicked.connect(self.calculate)

        # Add the widgets to a widget container
        widget_container = QWidget()
        layout = QVBoxLayout(widget_container)
        layout.addWidget(self.collector_label)
        layout.addWidget(self.collector_input)
        layout.addWidget(self.base_label)
        layout.addWidget(self.base_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.canvas)

        # Set the widget container as the central widget
        self.setCentralWidget(widget_container)

    def calculate(self):
        # Retrieve the collector and base voltages from the UI
        collector_voltage = float(self.collector_input.text())
        base_voltage = float(self.base_input.text())

        # Calculate the resulting voltages and currents
        dc_points = []
        ac_points = []
        for vce in np.arange(0, 10.1, 0.1):
            ic_dc, ic_ac = self.calculate_current(collector_voltage, base_voltage, vce)
            dc_points.append((vce, ic_dc))
            ac_points.append((vce, ic_ac))

        # Update the plot with the resulting voltages and currents
        self.ax.clear()
        self.ax.plot([p[0] for p in dc_points], [p[1] for p in dc_points], label="DC")
        self.ax.plot([p[0] for p in ac_points], [p[1] for p in ac_points], label="AC")
        self.ax.legend()
        self.canvas.draw()

    def calculate_current(self, Vc, Vb, Vce):
        beta = 100
        Vbe = 0.7
        Vt = 0.025
        R1 = 2200
        R2 = 6800
        RC = 1000
        RE = 220
        RL = 4700
        Vin = 10

        # Calculate the DC current through the transistor
        ic = (Vin - Vb - Vbe) / ((R1 / (R1 + R2)) * (1 + beta) * RE + RC)
        if ic < 0:
            ic = 0

        # Calculate the AC current through the transistor
        ic_ac = ic * np.sqrt(1 + (beta * (Vce - Vbe)) / (2 * Vt * np.log(1 + abs(beta * (Vce - Vbe)) / (2 * Vt))))

        return ic, ic_ac


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()






