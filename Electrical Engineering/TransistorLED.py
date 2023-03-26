import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QSpinBox, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("LED Circuit Calculator")

        # Create spin boxes for input values
        self.voltage_spinbox = QSpinBox()
        self.voltage_spinbox.setRange(0, 100)
        self.voltage_spinbox.setValue(9)
        self.current_spinbox = QSpinBox()
        self.current_spinbox.setRange(0, 100)
        self.current_spinbox.setValue(20)

        # Create button to calculate values
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        # Create label to display output values
        self.output_label = QLabel()

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Power Supply Voltage (V)"))
        layout.addWidget(self.voltage_spinbox)
        layout.addWidget(QLabel("LED Current (mA)"))
        layout.addWidget(self.current_spinbox)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.output_label)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set window size
        self.setGeometry(100, 100, 600, 400)

    def calculate(self):
        # Get input values
        voltage = self.voltage_spinbox.value()
        current = self.current_spinbox.value()

        # Calculate resistor value and power
        resistor_value = (voltage - 2) / (current / 1000)
        resistor_power = resistor_value * (current / 1000) ** 2

        # Display output values
        self.output_label.setText(f"Resistor Value: {resistor_value:.2f} ohms\nResistor Power: {resistor_power:.2f} watts")

        # Create and display graph
        plt.figure()
        plt.plot([0, voltage], [0, current])
        plt.xlabel("Voltage (V)")
        plt.ylabel("Current (mA)")
        plt.title("LED Circuit Characteristics")
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
