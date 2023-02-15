import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt

import pyqtgraph as pg


# Create the widget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.setWindowTitle("Voltage Amplification Circuit")
        self.setGeometry(100, 100, 800, 600)

        self.input_label = QLabel("Input Voltage:", self)
        self.input_label.move(50, 50)

        self.input_lineedit = QLineEdit(self)
        self.input_lineedit.move(150, 50)
        self.input_lineedit.resize(100, 30)

        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.move(300, 50)
        self.calculate_button.clicked.connect(self.calculate)

        self.plot_widget = pg.PlotWidget(self)
        self.plot_widget.move(50, 100)
        self.plot_widget.resize(700, 400)
        self.plot_widget.setBackground("w")
        self.plot_widget.showGrid(x=True, y=True)
        self.plot_widget.setLabel("left", "Voltage (V)")
        self.plot_widget.setLabel("bottom", "Input Voltage (V)")

        # Initialize the plot data
        self.plot_data = pg.PlotDataItem(pen=pg.mkPen("b", width=2))
        self.plot_widget.addItem(self.plot_data)

    # Calculate the output voltage
    def calculate(self):
        input_voltage_str = self.input_lineedit.text()
        try:
            input_voltage = float(input_voltage_str)
        except ValueError:
            return

        r1 = 10000
        r2 = 10000
        vcc = 12
        vbe = 0.7
        hfe = 100

        base_voltage = input_voltage * r2 / (r1 + r2)
        collector_voltage = vcc - (hfe + 1) * base_voltage - vbe
        output_voltage = collector_voltage

        self.plot_data.setData(*self.generate_data_points(input_voltage, output_voltage))

    # Generate the data points for the plot
    def generate_data_points(self, input_voltage, output_voltage):
        num_points = 100
        delta = 0.1

        x = [input_voltage - delta * num_points / 2 + i * delta for i in range(num_points)]
        y = [self.calculate_output_voltage(v) for v in x]

        return x, y

    # Calculate the output voltage
    def calculate_output_voltage(self, input_voltage):
        r1 = 10000
        r2 = 10000
        vcc = 12
        vbe = 0.7
        hfe = 100

        base_voltage = input_voltage * r2 / (r1 + r2)
        collector_voltage = vcc - (hfe + 1) * base_voltage - vbe
        return collector_voltage


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
