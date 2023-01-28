import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np


class DiodeGraph(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diode Behavior")

        # Create a user input for diode current
        self.current_input = QtWidgets.QLineEdit(self)
        self.current_input.move(20, 20)
        self.current_input.resize(100, 30)

        # Create a button to submit the user input
        self.submit_button = QtWidgets.QPushButton("Submit", self)
        self.submit_button.move(130, 20)
        self.submit_button.clicked.connect(self.display_graph)

        self.show()

    def display_graph(self):
        # Get the user input for diode current
        current = float(self.current_input.text())

        # Calculate the diode voltage
        voltage = 0.7 + np.log(current)

        # Plot the diode behavior on a graph
        plt.plot(current, voltage)
        plt.title("Diode Behavior")
        plt.xlabel("Current (A)")
        plt.ylabel("Voltage (V)")
        plt.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    graph = DiodeGraph()
    sys.exit(app.exec_())
