import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.axes = None
        self.setWindowTitle("Emitter Circuit Calculator")
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.verticalLayout = QVBoxLayout(self.centralWidget)

        # Set up the input fields
        self.collectorVoltageLabel = QLabel("Collector Voltage (V):")
        self.collectorVoltageTextBox = QLineEdit()
        self.baseVoltageLabel = QLabel("Base Voltage (V):")
        self.baseVoltageTextBox = QLineEdit()
        self.emitterResistorLabel = QLabel("Emitter Resistor (Ohm):")
        self.emitterResistorTextBox = QLineEdit()
        self.calculateButton = QPushButton("Calculate")
        self.calculateButton.clicked.connect(self.calculate)

        inputLayout = QVBoxLayout()
        inputLayout.addWidget(self.collectorVoltageLabel)
        inputLayout.addWidget(self.collectorVoltageTextBox)
        inputLayout.addWidget(self.baseVoltageLabel)
        inputLayout.addWidget(self.baseVoltageTextBox)
        inputLayout.addWidget(self.emitterResistorLabel)
        inputLayout.addWidget(self.emitterResistorTextBox)
        inputLayout.addWidget(self.calculateButton)

        # Set up the output fields
        self.emitterVoltageLabel = QLabel("Emitter Voltage (V):")
        self.emitterVoltageTextBlock = QLabel()
        self.collectorCurrentLabel = QLabel("Collector Current (A):")
        self.collectorCurrentTextBlock = QLabel()
        self.baseCurrentLabel = QLabel("Base Current (A):")
        self.baseCurrentTextBlock = QLabel()

        outputLayout = QVBoxLayout()
        outputLayout.addWidget(self.emitterVoltageLabel)
        outputLayout.addWidget(self.emitterVoltageTextBlock)
        outputLayout.addWidget(self.collectorCurrentLabel)
        outputLayout.addWidget(self.collectorCurrentTextBlock)
        outputLayout.addWidget(self.baseCurrentLabel)
        outputLayout.addWidget(self.baseCurrentTextBlock)

        # Set up the plot
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        plotLayout = QHBoxLayout()
        plotLayout.addWidget(self.canvas)

        # Add the input fields, output fields, and plot to the main layout
        self.verticalLayout.addLayout(inputLayout)
        self.verticalLayout.addLayout(outputLayout)
        self.verticalLayout.addLayout(plotLayout)

        # Initialize the plot
        self.plotData([], [], [], [], [], [])

    def calculate(self):
        # Get the input values
        collectorVoltage = float(self.collectorVoltageTextBox.text())
        baseVoltage = float(self.baseVoltageTextBox.text())
        emitterResistor = float(self.emitterResistorTextBox.text())

        # Calculate the output values for an emitter circuit
        emitterVoltage = baseVoltage - collectorVoltage
        collectorCurrent = emitterVoltage / emitterResistor
        baseCurrent = collectorCurrent / (pow(2.71828, emitterVoltage / (0.026 * 300)) - 1)

        # Update the output values in the UI
        self.emitterVoltageTextBlock.setText("{:.2f}".format(emitterVoltage))
        self.collectorCurrentTextBlock.setText("{:.4f}".format(collectorCurrent))
        self.baseCurrentTextBlock.setText("{:.4f}".format(baseCurrent))

        # Update the plot
        self.updatePlot(collectorCurrent, emitterResistor, baseVoltage, baseCurrent)

    def plotData(self, x1, y1, x2, y2, x3, y3):
        self.figure.clear()
        self.axes = self.figure.add_subplot(111)
        self.axes.plot(x1, y1, "r")
        self.axes.plot(x2, y2, "b")
        self.axes.plot(x3, y3, "g")
        self.axes.set_xlabel("Collector Current (A)")
        self.axes.set_ylabel("Emitter Voltage (V)")
        self.canvas.draw()

    def updatePlot(self, collectorCurrent, emitterResistor, baseVoltage, baseCurrent):
        # Calculate the data points for the plot
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        x3 = []
        y3 = []
        for i in range(0, 1000):
            x1.append(i / 1000)
            y1.append(x1[i] * emitterResistor)
            x2.append(i / 1000)
            y2.append(baseVoltage - y1[i])
            x3.append(i / 1000)
            y3.append(baseVoltage - (x3[i] * emitterResistor))

        # Update the plot
        self.plotData(x1, y1, x2, y2, x3, y3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())