import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
import matplotlib.pyplot as plt
import numpy as np


class DiodeCurveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)
        self.diodeTypeLineEdit = QLineEdit(self.centralWidget)
        self.layout.addWidget(self.diodeTypeLineEdit)
        self.plotPushButton = QPushButton("Plot", self.centralWidget)
        self.layout.addWidget(self.plotPushButton)
        self.plotPushButton.clicked.connect(self.plot)
        self.setWindowTitle("Diode Curve Plotter")
        self.show()

    def plot(self):
        diodeType = self.diodeTypeLineEdit.text()
        if diodeType == "silicon":
            reverseVoltage = np.linspace(-10, 0, 1000)
            current = np.exp(reverseVoltage)
        elif diodeType == "germanium":
            reverseVoltage = np.linspace(-10, 0, 1000)
            current = 2 * np.exp(reverseVoltage)
        elif diodeType == "shottky":
            reverseVoltage = np.linspace(-10, 0, 1000)
            current = 3 * np.exp(reverseVoltage)
        else:
            reverseVoltage = np.linspace(-10, 0, 1000)
            current = np.zeros(1000)
        plt.plot(reverseVoltage, current)
        plt.xlabel("Reverse Voltage (V)")
        plt.ylabel("Current (A)")
        plt.title(f"{diodeType.capitalize()} Diode Characteristic")
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    diodeCurveWindow = DiodeCurveWindow()
    sys.exit(app.exec())
