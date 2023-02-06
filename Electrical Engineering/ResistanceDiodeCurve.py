import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class DiodeGraph(QMainWindow):
    # get the user input for voltage and resistance
    def __init__(self):
        # get the user input for voltage and resistance
        super().__init__()
        self.setWindowTitle("Diode Behavior")
        self.label_v = QLabel("Voltage [V]:")
        self.input_v = QLineEdit()
        self.label_i = QLabel("Resistance [Ohm]:")
        self.input_i = QLineEdit()
        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.display_graph)
        layout = QVBoxLayout()
        layout.addWidget(self.label_v)
        layout.addWidget(self.input_v)
        layout.addWidget(self.label_i)
        layout.addWidget(self.input_i)
        layout.addWidget(self.button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

    def display_graph(self):
        voltage = float(self.input_v.text())
        resistance = float(self.input_i.text())
        # calculate the diode voltage
        current = np.arange(0, 0.1, 0.001)
        voltage = 0.7 + np.log(current)
        # plot the diode behavior on a graph
        plt.plot(current, voltage)
        plt.title("Diode Behavior")
        plt.xlabel("Current (A)")
        plt.ylabel("Voltage (V)")
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = DiodeGraph()
    sys.exit(app.exec_())
