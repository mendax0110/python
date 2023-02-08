import sys
from PyQt6 import QtWidgets, QtGui, QtCore
import numpy as np
import matplotlib.pyplot as plt


# Create the widget
class PhasorPlot(QtWidgets.QWidget):

    # Initialize the widget
    def __init__(self):
        super().__init__()

        self.real_input = QtWidgets.QLineEdit()
        self.imag_input = QtWidgets.QLineEdit()
        self.plot_button = QtWidgets.QPushButton("Plot Phasor")
        self.plot_button.clicked.connect(self.plot_phasor)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Enter real component:"))
        layout.addWidget(self.real_input)
        layout.addWidget(QtWidgets.QLabel("Enter imaginary component:"))
        layout.addWidget(self.imag_input)
        layout.addWidget(self.plot_button)
        self.setLayout(layout)

    # Plot the phasor
    def plot_phasor(self):
        real = float(self.real_input.text())
        imag = float(self.imag_input.text())
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.arrow(0, 0, real, imag, head_width=0.2, head_length=0.2, fc='red', ec='red')
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.show()


# Create the application
app = QtWidgets.QApplication(sys.argv)
phasor_plot = PhasorPlot()
phasor_plot.show()
sys.exit(app.exec())
