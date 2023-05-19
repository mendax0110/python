import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window properties
        self.setWindowTitle("Circuit Calculator")
        self.setGeometry(100, 100, 400, 300)

        # create a widget to hold the circuit diagram
        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        # create a horizontal layout to hold the circuit diagram and the input fields
        self.layout = QHBoxLayout()
        self.widget.setLayout(self.layout)

        # create a graphics view to hold the circuit diagram
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.view.setSceneRect(0, 0, 200, 100)

        # add a voltage source to the scene
        self.voltage_source = self.scene.addRect(QRectF(10, 40, 20, 20), QPen(Qt.black), QBrush(Qt.yellow))
        self.voltage_source.setFlag(QGraphicsItem.ItemIsSelectable)
        self.voltage_label = self.scene.addText("V", QFont("Arial", 12))
        self.voltage_label.setPos(32, 45)

        # add a resistor to the scene
        self.resistor = self.scene.addRect(QRectF(100, 30, 30, 40), QPen(Qt.black), QBrush(Qt.gray))
        self.resistor.setFlag(QGraphicsItem.ItemIsSelectable)
        self.resistor_label = self.scene.addText("R", QFont("Arial", 12))
        self.resistor_label.setPos(82, 45)

        # create a vertical layout to hold the input fields
        self.input_layout = QVBoxLayout()

        # create a label and a text box for the voltage input
        self.voltage_label = QLabel("Voltage (V):")
        self.voltage_input = QLineEdit()
        self.input_layout.addWidget(self.voltage_label)
        self.input_layout.addWidget(self.voltage_input)

        # create a label and a text box for the resistance input
        self.resistance_label = QLabel("Resistance (Ω):")
        self.resistance_input = QLineEdit()
        self.input_layout.addWidget(self.resistance_label)
        self.input_layout.addWidget(self.resistance_input)

        # create a label and a text box for the current input
        self.current_label = QLabel("Current (mA):")
        self.current_input = QLineEdit()
        self.input_layout.addWidget(self.current_label)
        self.input_layout.addWidget(self.current_input)

        # create a label and a text box for the power input
        self.power_label = QLabel("Power (mW):")
        self.power_input = QLineEdit()
        self.input_layout.addWidget(self.power_label)
        self.input_layout.addWidget(self.power_input)

        # create a button to calculate the missing value
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        self.input_layout.addWidget(self.calculate_button)

        # add the circuit diagram and the input fields to the main layout
        self.layout.addWidget(self.view)
        self.layout.addLayout(self.input_layout)

        self.calculation_history = QTextEdit()
        self.calculation_history.setReadOnly(True)
        self.input_layout.addWidget(self.calculation_history)

    def calculate(self):
        voltage = self.voltage_input.text()
        resistance = self.resistance_input.text()
        current = self.current_input.text()

        try:
            # check if voltage and resistance are both valid inputs
            if voltage and resistance:
                voltage = float(voltage)
                resistance = float(resistance)
                current = voltage / resistance
                power = voltage * current
                self.current_label.setText(f"Current (mA): {current * 1000:.2f}")
                self.power_label.setText(f"Power (mW): {power * 1000:.2f}")

            # check if voltage and current are both valid inputs
            elif voltage and current:
                voltage = float(voltage)
                current = float(current)
                resistance = voltage / current
                power = voltage * current
                self.resistance_label.setText(f"Resistance (Ω): {resistance:.2f}")
                self.power_label.setText(f"Power (mW): {power * 1000:.2f}")

            # check if resistance and current are both valid inputs
            elif resistance and current:
                resistance = float(resistance)
                current = float(current)
                voltage = resistance * current
                power = voltage * current
                self.voltage_label.setText(f"Voltage (V): {voltage:.2f}")
                self.power_label.setText(f"Power (mW): {power * 1000:.2f}")

            # if only one input is valid, clear the other two
            else:
                self.voltage_label.setText("Voltage (V):")
                self.resistance_label.setText("Resistance (Ω):")
                self.current_label.setText("Current (mA):")
                self.power_label.setText("Power (mW):")

            # update the calculation history textbox
            calculation_str = f"V = {voltage:.2f} V, R = {resistance:.2f} Ω, I = {current * 1000:.2f} mA, P = {power * 1000:.2f} mW\n"
            self.calculation_history.insertPlainText(calculation_str)

        except ValueError:
            # if the inputs are invalid, clear all the labels
            self.voltage_label.setText("Voltage (V):")
            self.resistance_label.setText("Resistance (Ω):")
            self.current_label.setText("Current (mA):")
            self.power_label.setText("Power (mW):")


# create the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
