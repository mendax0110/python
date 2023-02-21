import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.setWindowTitle("Voltage Divider with Bipolar Transistor")
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)
        layout = QtWidgets.QVBoxLayout()
        centralWidget.setLayout(layout)

        # Add the plot widget
        self.plotWidget = pg.PlotWidget()
        layout.addWidget(self.plotWidget)

        # Add the voltage and transistor series to the plot
        self.voltageSeries = pg.PlotDataItem(pen=QColor(Qt.blue))
        self.plotWidget.addItem(self.voltageSeries)
        self.transistorSeries = pg.PlotDataItem(pen=QColor(Qt.red))
        self.plotWidget.addItem(self.transistorSeries)

        # Add the axis labels
        self.plotWidget.setLabel('bottom', "Time (s)")
        self.plotWidget.setLabel('left', "Voltage (V)")

        # Add the input fields and button
        inputLayout = QtWidgets.QHBoxLayout()
        layout.addLayout(inputLayout)
        inputLayout.addWidget(QtWidgets.QLabel("Voltage (V):"))
        self.voltageInput = QtWidgets.QLineEdit()
        inputLayout.addWidget(self.voltageInput)
        inputLayout.addWidget(QtWidgets.QLabel("Resistor 1 (Ω):"))
        self.resistor1Input = QtWidgets.QLineEdit()
        inputLayout.addWidget(self.resistor1Input)
        inputLayout.addWidget(QtWidgets.QLabel("Resistor 2 (Ω):"))
        self.resistor2Input = QtWidgets.QLineEdit()
        inputLayout.addWidget(self.resistor2Input)
        inputLayout.addWidget(QtWidgets.QLabel("Beta (β):"))
        self.betaInput = QtWidgets.QLineEdit()
        inputLayout.addWidget(self.betaInput)
        self.calculateButton = QtWidgets.QPushButton("Calculate")
        inputLayout.addWidget(self.calculateButton)

        # Connect the button to the calculate function
        self.calculateButton.clicked.connect(self.calculate)

    def calculate(self):
        # Retrieve the input values
        voltage = float(self.voltageInput.text())
        r1 = float(self.resistor1Input.text())
        r2 = float(self.resistor2Input.text())
        beta = float(self.betaInput.text())

        # Calculate the voltage divider and bipolar transistor values
        time = [0, r2 * 1e3 / (r1 + r2) * 10e-6, r2 * 1e3 / (r1 + r2) * 10e-6 + 1e-6, 1e-3]
        voltageDivider = [voltage, voltage * r2 / (r1 + r2), voltage * r2 / (r1 + r2) * (1 - beta), 0]
        transistor = [voltage, voltage * r2 / (r1 + r2), 0, 0]

        # Update the series data
        self.voltageSeries.setData(time, voltageDivider)
        self.transistorSeries.setData(time, transistor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
