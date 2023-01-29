import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import matplotlib.pyplot as plt
import numpy as np


class DiodenSchaltung(QMainWindow):
    def __init__(self):
        super().__init__()

        # GUI-Elemente erstellen
        self.label_v = QLabel("Spannung [V]:")
        self.input_v = QLineEdit()
        self.label_i = QLabel("Strom [A]:")
        self.input_i = QLineEdit()
        self.button = QPushButton("Kennlinie berechnen")
        self.button.clicked.connect(self.show_kennlinie)

        # GUI-Elemente anordnen
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

    def show_kennlinie(self):
        v_max = float(self.input_v.text())
        i_max = float(self.input_i.text())

        # Berechnung der Kennlinie
        v = np.linspace(0, v_max, 100)
        i = i_max * (np.exp(v / 0.025) - 1)

        # Plot der Kennlinie
        plt.plot(v, i)
        plt.xlabel("Spannung [V]")
        plt.ylabel("Strom [A]")
        plt.title("Kennlinie")
        plt.show()


app = QApplication(sys.argv)
dioden_schaltung = DiodenSchaltung()
sys.exit(app.exec_())
