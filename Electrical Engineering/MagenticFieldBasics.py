import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QDoubleSpinBox, QPushButton
from PyQt5.uic.properties import QtGui, QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Magnetfeld")
        self.setGeometry(100, 100, 400, 300)

        self.h_label = QLabel("H:")
        self.h_spinbox = QDoubleSpinBox()
        self.h_spinbox.setRange(0, 100)

        self.b_label = QLabel("B:")
        self.b_spinbox = QDoubleSpinBox()
        self.b_spinbox.setRange(0, 100)

        self.theta_label = QLabel("Theta:")
        self.theta_spinbox = QDoubleSpinBox()
        self.theta_spinbox.setRange(0, 360)

        self.calculate_button = QPushButton("Berechnen")
        self.calculate_button.clicked.connect(self.calculate_magnetic_field)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.h_label, 0, 0)
        self.grid_layout.addWidget(self.h_spinbox, 0, 1)
        self.grid_layout.addWidget(self.b_label, 1, 0)
        self.grid_layout.addWidget(self.b_spinbox, 1, 1)
        self.grid_layout.addWidget(self.theta_label, 2, 0)
        self.grid_layout.addWidget(self.theta_spinbox, 2, 1)
        self.grid_layout.addWidget(self.calculate_button, 3, 0, 1, 2)

        self.central_widget = QLabel()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)

        self.statusBar().showMessage("Bitte geben Sie die Werte ein und klicken Sie auf 'Berechnen'.")

        self.error_message = None

    def calculate_magnetic_field(self):
        try:
            h = self.h_spinbox.value()
            b = self.b_spinbox.value()
            theta = math.radians(self.theta_spinbox.value())

            x = np.linspace(-h, h, 20)
            y = np.linspace(-h, h, 20)
            X, Y = np.meshgrid(x, y)
            U = b * np.cos(theta) + h * np.cos(theta) * (Y / h) ** 2
            V = b * np.sin(theta) + h * np.sin(theta) * (X / h) ** 2

            plt.figure()
            plt.streamplot(X, Y, U, V, density=1.5, color='b')
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Magnetfeld")
            plt.grid(True)
            plt.show()

            self.error_message = None
            self.statusBar().showMessage("Berechnung erfolgreich.")

        except Exception as e:
            self.error_message = str(e)
            self.statusBar().showMessage("Fehler bei der Berechnung.")

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.error_message:
            painter = QtGui.QPainter(self.central_widget)
            painter.drawText(self.central_widget.rect(), QtCore.Qt.AlignCenter, self.error_message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

