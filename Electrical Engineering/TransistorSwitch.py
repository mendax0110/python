import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Switch Simulator")
        self.setGeometry(100, 100, 800, 600)

        # Set up the main widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Set up the layout
        layout = QVBoxLayout(main_widget)

        # Add the matplotlib figure canvas to the layout
        figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(figure)
        layout.addWidget(self.canvas)

        # Add input boxes for the user to enter the input voltage and resistance
        input_voltage_label = QLabel("Input Voltage (V):")
        self.input_voltage_edit = QLineEdit()
        resistance_label = QLabel("Resistance (Ω):")
        self.resistance_edit = QLineEdit()
        layout.addWidget(input_voltage_label)
        layout.addWidget(self.input_voltage_edit)
        layout.addWidget(resistance_label)
        layout.addWidget(self.resistance_edit)

        # Add a button to update the plot
        button = QPushButton("Switch")
        button.clicked.connect(self.update_plot)
        layout.addWidget(button)

        # Set up the initial plot
        self.plot(figure, 1.0)

    def plot(self, figure, input_voltage):
        # Create a subplot for the voltage graph
        voltage_subplot = figure.add_subplot(111)
        voltage_subplot.set_xlabel("Time (ms)")
        voltage_subplot.set_ylabel("Voltage (V)")
        voltage_subplot.set_title("Voltage Graph")

        # Calculate the output voltage
        time = [i / 10.0 for i in range(361)]
        input_voltage_values = [input_voltage * math.sin(i * math.pi / 180.0) for i in range(361)]

        # Check if the resistance field is not blank
        if self.resistance_edit.text() != '':
            # Convert the resistance value to float
            resistance = float(self.resistance_edit.text())
        else:
            # Set default resistance value if field is blank
            resistance = 1.0

        output_voltage_values = [self.calculate_output_voltage(v) for v in input_voltage_values]

        # Plot the output voltage
        voltage_subplot.plot(time, output_voltage_values, label="Output Voltage")
        voltage_subplot.legend()

        # Draw the plot
        self.canvas.draw()

    def update_plot(self):
        # Check if the input voltage field is not blank
        if self.input_voltage_edit.text() != '':
            # Convert the input voltage value to float
            input_voltage = float(self.input_voltage_edit.text())
        else:
            # Set default input voltage value if field is blank
            input_voltage = 1.0

        # Clear the plot and redraw with updated values
        self.canvas.figure.clear()
        self.plot(self.canvas.figure, input_voltage)

    def calculate_output_voltage(self, input_voltage):
        if self.resistance_edit.text() != '':
            resistance = float(self.resistance_edit.text())
        else:
            resistance = 1.0
        beta = 100.0
        base_voltage = 0.7
        saturation_voltage = 0.2
        current = (input_voltage - base_voltage) / resistance
        output_voltage = max(0, min(beta * current, saturation_voltage)) * resistance
        return output_voltage


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
